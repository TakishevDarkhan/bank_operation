import json
from datetime import datetime

def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtered(data):
    filtered_operations = []
    for x in data:
        if x.get("state") == "EXECUTED":
            filtered_operations.append(x)
    return filtered_operations

def data_sorted(data):
    return sorted(data, key=lambda x: x["date"], reverse=True)[:5]

def _hide_order(order):
    if len(order) == 16:
        return f"{order[:4]} {order[4:6]}** **** {order[-4:]}"
    return f"**{order[-4:]}"

def _data_reverse(date):
    return ".".join(date.split('T')[0].split("-")[::-1])

def output_last_operation(data):
    for operation in data:
        date = _data_reverse(operation["date"])
        print(f"{date} {operation['description']}")
        if operation.get('from'):
            order_from = operation['from'].split()
            print(f"{' '.join(order_from[:-1])} {_hide_order(order_from[-1])} -> ", end='')
        order_to = operation['to'].split()
        print(f"{' '.join(order_to[:-1])} {_hide_order(order_to[-1])}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")





