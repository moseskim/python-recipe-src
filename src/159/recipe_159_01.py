text1 = "abc123"
text2 = "123"

# ascii만 포함하는가
print(str.isascii(text1))
print(str.isascii(text2))

# 10진수 숫자만 포함하는가
print(str.isdecimal(text1))
print(str.isdecimal(text2))
