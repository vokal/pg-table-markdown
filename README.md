A command line tool that generates markdown documentation for Postgres tables in a given schema

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
