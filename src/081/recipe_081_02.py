def add_message(f):
    """ 함수 앞뒤로 시작/종료 메시지를 추가한다 """

    def new_func(*args, **kwargs):
        print("처리를 시작합니다.")
        result = f(*args, **kwargs)
        print("처리를 종료합니다.")
        return result

    return new_func


# add_one에 대해 데커레이터 처리 추가
@add_message
def add_one(num):
    print("파라미터: {}".format(num))
    return num + 1


# add_one 실행
result = add_one(1)
print("반환값: {}".format(result))
