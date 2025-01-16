import json


def read_json(file_name):
    try:
        with open(f"data/{file_name}", 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_json(file_name, data):
    with open(f"data/{file_name}", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)