def is_odd(n):
    """ 홀수 판정 함수 """
    return (n % 2) == 1


l1 = [1, 2, 4, 5, 6, 10, 11]
ft = filter(is_odd, l1)
l2 = list(ft)
print(l2)
