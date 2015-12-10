from setuptools import setup


setup(
    name='pg-table-markdown',
    version='1.0.0',
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
