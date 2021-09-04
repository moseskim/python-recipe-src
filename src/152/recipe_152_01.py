# 중괄호만 사용
text = "안녕하세요, {}님. 지금은 {}시입니다."
name = "JPUB"
time = 10

ftext = text.format(name, time)
print(ftext)

# 필드 번호
text = "안녕하세요, {0}님. 지금은 {1}시입니다."
name = "JPUB"
time = 10

ftext = text.format(name, time)
print(ftext)


# 필드명
text = "안녕하세요, {name}님. 지금은 {time}시입니다."
name = "JPUB"
time = 10

ftext1 = text.format(name=name, time=time)
print(ftext1)
