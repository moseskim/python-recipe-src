d = {"key1": 100, "key2": 200}
# 존재하는 키를 지정
val1 = d.get("key1")
print(val1)

# 존재하지 않는 키를 지정
val2 = d.get("keyX")
print(val2)

# 위 코드의 계속
val3 = d.get("keyX", 999)
print(val3)
