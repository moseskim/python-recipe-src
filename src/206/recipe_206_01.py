import json

data_dict = {'colors': ['red', 'green', 'blue'], 'items': [123, 456, 789],
             'users': [{'name': '제이펍', 'id': 1}, {'name': '출판사', 'id': 5}]}
json_str = json.dumps(data_dict, indent=2, ensure_ascii=False)
print(json_str)
