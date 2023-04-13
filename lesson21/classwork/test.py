import json

with open('output.json') as file:
    json_data = json.load(file)


record_id: int | str

if len(json_data) == 0:
    record_id = '0'
else:
    record_id = int(list(json_data.keys())[-1]) + 1
