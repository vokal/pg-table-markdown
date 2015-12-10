from collections import defaultdict


def parse_schema_data(schema_data):
    output = defaultdict(list)
    for i in schema_data:
        table_name = i.pop('table_name')
        output[table_name].append(i)
    return output
