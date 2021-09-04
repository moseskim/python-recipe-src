def func(x, y, *args):
    print(f"첫 번째 인수: {x}")
    print(f"두 번째 인수: {y}")
    if args:
        print(f"세 번째 이후의 인수: {args}")


func(1, 2)
print("-----")
func(1, 2, 3, 4, 5)
