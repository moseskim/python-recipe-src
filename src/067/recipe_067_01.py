import math

l = [1, 64, 9, -49, 100]
for x in l:
    if x < 0:
        print(f"{x}은(는) 음수이므로 계산할 수 없습니다. 처리를 건너 뜁니다.")
        continue
    s = math.sqrt(x)
    print(s)
