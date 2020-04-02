import json
import os


def get_table():
    table_file = open("synthetic_table.json", encoding='UTF-8')
    table_raw = table_file.read()

    table_file.close()

    return json.loads(table_raw)
