import numbers


def calc10times(num):
    if not isinstance(num, numbers.Number):
        raise TypeError('파리미터가 올바르지 않습니다.')

    return num * 10


val = calc10times(10)
print(val)
val = calc10times('abc')
print(val)
