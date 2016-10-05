A command line tool that generates Markdown documentation for Postgres tables in a given schema.

## Installation
```
pip install pg-table-markdown
```

_Note:_ Since `pg-table-markdown` is intended to connect to Postgres databases, it has a dependedncy on `psycopg2`. However, `psycopg2` includes compiled C modules, and therefore may require compiling from source if it's not already installed. Installing via `pip` will require `python-dev` and `libpq-dev`. `psycopg2` maintainers generally recommend [installing from binary](http://initd.org/psycopg/docs/install.html#install-from-package) instead.


## Usage
```
Usage: pgtablemd [OPTIONS]

  Export Postgres table documentation to a markdown file

Options:
  --database_url TEXT  Database connection URL
  --table_schema TEXT  Postgres table_schema, default is: public
  --output_file TEXT   Path for generated markdown file
  --max_length         To display maximum length of character varying, default is: False
  --help               Show this message and exit.
```

**Note:**
For those unfamiliar with Postgres database connection URLs, they use the following format:
```
postgres://username:password@host:port/dbname
```


## Sample Output

The generated Markdown details the column name, type, and default value for each table defined in your schema. It also displays nicely in GitHub (see more [here](./SAMPLE_TABLES.md)).

### app_users 

Column | Type | Default | Nullable 
--- | --- | --- | --- 
id | integer | nextval('app_users_id_seq'::regclass) | NO 
email | character varying | None | NO 
password | character varying | None | YES 
is_active | boolean | true | YES 
is_admin | boolean | false | YES 


## Run tests with Docker Compose
```
docker-compose run cli nosetests -v
```
