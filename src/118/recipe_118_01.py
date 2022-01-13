# 비교 연산자

x = 0
y = 1
z = 2

if x < y < z:
    print("적정 범위 안입니다.")

# 복수 판정
name = "화약"
if name in ("연료", "화약"):
    print("운송할 수 없습니다.")

# True 판정
flg = True
if flg:
    print("플래그가 ON입니다.")

# 삼항 연산자
x = 200 if flg else 100

# 루프
data = (1, 2, 3, 4,)
for val in data:
    print(val)

# 동시 대입
text1 = text2 = text3 = "init value"

# 리스트 컴프리헨션
l1 = [7, 11, 2, 5, 10, 3]
l2 = [val * 2 for val in l1]

# 부적절한 변수명
# sum = x + y NG 예: 이후 sum 함수를 사용할 수 없게 된다
sum_val = x + y

# 변수 치환
x, y = y, x
