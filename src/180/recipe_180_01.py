# 숫잣값을 2배하는 함수
def calc_double(n):
    return n * 2


l1 = [1, 3, 6, 50, 5]

# map 함수를 사용해 l1의 모든 요소를 2배하여 map1에 저장
map1 = map(calc_double, l1)

# map 타입을 list 타입으로 변환해 l2에 저장
l2 = list(map1)

print(l2)
