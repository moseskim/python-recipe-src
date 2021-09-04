import json

json_text = """
{
  "colors": [ "red", "green", "blue" ],
  "items": [ 123, 456, 789 ],
  "users": [
    { "name": "제이펍", "id": 1 },
    { "name": "출판사", "id": 5 }
  ]
}
"""
data_dict = json.loads(json_text)
# 결과 딕셔너리 전체 표시
print(data_dict)

# colors 키를 지정하고 0번째 요소를 얻음
print(data_dict["colors"][0])

# users 키를 지정하고 0번째 요소를 얻음
print(data_dict["users"][0]["id"])
