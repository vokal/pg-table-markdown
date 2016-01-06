def build_schema_query(table_schema):
    schema_query = """
    SELECT      table_name,
                column_name,
                column_default,
                is_nullable,
                data_type,
                character_maximum_length
    FROM        information_schema.columns
    WHERE       table_schema = '{0}'
    ORDER BY    table_name,
                ordinal_position
    """.format(table_schema)
    return schema_query
