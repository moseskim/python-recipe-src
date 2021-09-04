def sum_abs(x, y):
    """ 두 숫자의 절댓값의 합을 구한다(버그 있음) """
    val = abs(x) + y
    assert val >= 0, "계산 결과가 음수입니다."
    return val


val1 = sum_abs(-200, 100)
print(val1)
val2 = sum_abs(100, -200)
print(val2)
