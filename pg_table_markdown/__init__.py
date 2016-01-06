import sys
import click
from pg_table_markdown.database import database_connection, UnableToConnectToDatabase
from pg_table_markdown.utils import parse_schema_data
from pg_table_markdown.queries import build_schema_query


SECTION_HEADING = '### {0} \n\n'
TABLE_HEADER = 'Column | Type | Default | Nullable \n'
TABLE_DIVIDER = '--- | --- | --- | --- \n'
TABLE_ROW = '{column_name} | {data_type} | {column_default} | {is_nullable} \n'


@click.command()
@click.option('--database_url', prompt=True, help='Database connection URL')
@click.option('--table_schema', default='public', help='Postgres table_schema, default is: public')
@click.option('--output_file', prompt=True, help='Path for generated markdown file')
def cli(database_url, table_schema, output_file):
    """
    Export Postgres table documentation to a markdown file
    """
    try:
        db = database_connection(database_url=database_url)
    except UnableToConnectToDatabase:
        click.echo("Unable to connect to database using 'database_url': {0}".format(database_url))
        sys.exit(1)

    cursor = db.cursor()
    cursor.execute(build_schema_query(table_schema=table_schema))
    results = cursor.fetchall()
    cursor.close()

    parsed = parse_schema_data(schema_data=results)
    with open(output_file, 'w') as f:
        for table_name in sorted(parsed.keys()):
            f.write(SECTION_HEADING.format(table_name))
            f.write(TABLE_HEADER)
            f.write(TABLE_DIVIDER)
            for column in parsed[table_name]:
                f.write(TABLE_ROW.format(**column))
            f.write('\n')
