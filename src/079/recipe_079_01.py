def outer_function():
    """ 외부 함수 """
    print('outer_function 실행')

    def inner_function():
        """ 내부 함수 """
        print('inner_function 실행')

    inner_function()


outer_function()
