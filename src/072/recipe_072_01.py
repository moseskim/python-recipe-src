def func(x, y, **kwargs):
    print(f"인수 x: {x}")
    print(f"인수 y: {y}")
    if kwargs:
        print(f"세 번째 이후의 인수: {kwargs}")


func(x=1, y=2)
print("-----")
func(x=1, y=2, z=3, w=4)
