import os
import subprocess
import unittest
import psycopg2


DATABASE_HOST = os.getenv('DB_PORT_5432_TCP_ADDR', '127.0.0.1')
DATABASE_PORT = os.getenv('DB_PORT_5432_TCP_PORT', '5432')
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'postgres'
DATABASE_NAME = 'postgres'
DATABASE_URL = 'postgres://{0}:{1}@{2}:{3}/{4}'.format(
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME)
OUTPUT_FILE = '/test/tables.md'
OUTPUT_FILE2 = '/test/tables_with_length.md'

def database_connection():
    connection = psycopg2.connect(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME)
    connection.set_session(autocommit=True)
    return connection


class CliTestCase(unittest.TestCase):

    def setUp(self):
        super(CliTestCase, self).setUp()
        self.build_table()

    def build_table(self):
        db = database_connection()
        create_table_query = """
        DROP TABLE IF EXISTS my_whatever;
        CREATE TABLE my_whatever
        (
            id          SERIAL PRIMARY KEY,
            stuff       TEXT NOT NULL
        );

        DROP TABLE IF EXISTS my_users;
        CREATE TABLE my_users
        (
            id          SERIAL PRIMARY KEY,
            email       TEXT NOT NULL,
            password    TEXT NOT NULL,
            display_name CHARACTER VARYING(256)
        );
        """
        cursor = db.cursor()
        cursor.execute(create_table_query)
        cursor.close()

    def test_generate_table_markdown(self):
        database_url = '--database_url={0}'.format(DATABASE_URL)
        table_schema = '--table_schema=public'
        output_file = '--output_file={0}'.format(OUTPUT_FILE)
        proc = subprocess.Popen(['pgtablemd', database_url, table_schema, output_file])
        proc.communicate()
        with open(OUTPUT_FILE, 'r') as f:
            result = f.readlines()

        self.assertEqual('### my_users \n', result[0])
        self.assertEqual('\n', result[1])
        self.assertEqual('Column | Type | Default | Nullable \n', result[2])
        self.assertEqual('--- | --- | --- | --- \n', result[3])
        self.assertEqual("id | integer | nextval('my_users_id_seq'::regclass) | NO \n", result[4])
        self.assertEqual('email | text | None | NO \n', result[5])
        self.assertEqual('password | text | None | NO \n', result[6])
        self.assertEqual('display_name | character varying | None | YES \n',result[7])
        self.assertEqual('\n', result[8])

        self.assertEqual('### my_whatever \n', result[9])
        self.assertEqual('\n', result[10])
        self.assertEqual('Column | Type | Default | Nullable \n', result[11])
        self.assertEqual('--- | --- | --- | --- \n', result[12])
        self.assertEqual("id | integer | nextval('my_whatever_id_seq'::regclass) | NO \n", result[13])
        self.assertEqual('stuff | text | None | NO \n', result[14])
        self.assertEqual('\n', result[15])

        output_file = '--output_file={0}'.format(OUTPUT_FILE2)
        max_length = '--max_length'
        proc = subprocess.Popen(['pgtablemd', database_url, table_schema, output_file, max_length])
        proc.communicate()
        with open(OUTPUT_FILE2, 'r') as f:
            result = f.readlines()

        self.assertEqual('### my_users \n', result[0])
        self.assertEqual('\n', result[1])
        self.assertEqual('Column | Type | Default | Nullable \n', result[2])
        self.assertEqual('--- | --- | --- | --- \n', result[3])
        self.assertEqual("id | integer | nextval('my_users_id_seq'::regclass) | NO \n", result[4])
        self.assertEqual('email | text | None | NO \n', result[5])
        self.assertEqual('password | text | None | NO \n', result[6])
        self.assertEqual('display_name | character varying(256) | None | YES \n',result[7])
        self.assertEqual('\n', result[8])

        self.assertEqual('### my_whatever \n', result[9])
        self.assertEqual('\n', result[10])
        self.assertEqual('Column | Type | Default | Nullable \n', result[11])
        self.assertEqual('--- | --- | --- | --- \n', result[12])
        self.assertEqual("id | integer | nextval('my_whatever_id_seq'::regclass) | NO \n", result[13])
        self.assertEqual('stuff | text | None | NO \n', result[14])
        self.assertEqual('\n', result[15])
