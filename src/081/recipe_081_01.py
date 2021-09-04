def add_message(f):
    """ 함수 앞뒤로 시작/종료 메시지를 추가한다 """

    def new_func():
        print("처리를 시작합니다.")
        f()
        print("처리를 종료합니다.")

    return new_func


def sample_func():
    """ 실행 메시지를 표시하는 함수 """
    print("sample_func의 처리를 실행합니다.")


# sample_func에 대해 처리를 추가한 함수를 얻는다
decorated_func = add_message(sample_func)

# 처리를 추가한 함수를 실행한다
decorated_func()
