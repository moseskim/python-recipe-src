text = r"aaa\nbbb\nccc"
print(text)
text = " abcdefg "

# 문자열 오른쪽 공백 제거
r_stripped = text.rstrip()
print("*" + r_stripped + "*")

# 문자열 왼쪽 공백 제거
l_stripped = text.lstrip()
print("*" + l_stripped + "*")
