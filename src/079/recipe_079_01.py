def outer_function():
    """ 바깥쪽 함수 """
    print('outer_function 실행')

    def inner_function():
        """ 안쪽 함수 """
        print('inner_function 실행')

    inner_function()


outer_function()
