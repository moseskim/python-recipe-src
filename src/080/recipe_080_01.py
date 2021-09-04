def outer_function():
    """ 외부 함수 """

    def inner_function():
        """ 내부 함수 """
        print('inner_function을 실행했습니다.')

    # 내부 함수를 반환값으로 반환
    return inner_function


func = outer_function()
func()
