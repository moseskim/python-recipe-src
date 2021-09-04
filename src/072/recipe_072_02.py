def func(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


print("---첫 번째 인수만 지정한 결과---")
func(1)

print("---길이가 변하는 인수를 지정한 결과---")
func(1, 100, 200, 300, a="X", b="Y", c="Z")
