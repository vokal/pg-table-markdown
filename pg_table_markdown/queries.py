def build_schema_query(table_schema):
    schema_query = """
    WITH table_schema_info AS (
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
    )
    SELECT      JSON_AGG(table_schema_info.*)
    FROM        table_schema_info;
    """.format(table_schema)
    return schema_query
