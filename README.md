A command line tool that generates markdown documentation for Postgres tables in a given schema

## Installation
```
pip install pg-table-markdown
```

## Usage
```
Usage: pgtablemd [OPTIONS]

  Export Postgres table documentation to a markdown file

Options:
  --database_url TEXT  Database connection URL
  --table_schema TEXT  Postgres table_schema, default is: public
  --output_file TEXT   Path for generated markdown file
  --help               Show this message and exit.
```

**Note:**
For those unfamiliar with Postgres database connection URLs, they use the following format:
```
postgres://username:password@host:port/dbname
```


## Run tests with Docker Compose
```
docker-compose run cli nosetests -v
```
