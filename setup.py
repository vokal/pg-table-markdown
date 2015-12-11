from setuptools import setup


setup(
    name='pg-table-markdown',
    version='1.0.2',
    author='Vokal',
    author_email='pypi@vokal.io',
    description='A command line tool that generates markdown documentation for Postgres tables in a given schema',
    url='https://github.com/vokal/pg-table-markdown',
    packages=['pg_table_markdown'],
    py_modules=['pg_table_markdown'],
    install_requires=[
        'Click==6.2',
        'psycopg2==2.6.1',
    ],
    entry_points='''
        [console_scripts]
        pgtablemd=pg_table_markdown:cli
    ''',
)
