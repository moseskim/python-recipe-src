def outer_function():
    """ 외부 함수 """

    count = 0

    def inner_function():
        """ 내부 함수 """
        nonlocal count
        count += 1
        print("실행 횟수: {}회".format(count))

    return inner_function


# 함수 객체를 얻음
func1 = outer_function()

# 함수 실행
func1()
func1()
func1()
