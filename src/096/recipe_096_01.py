def div_num(a, b):
    try:
        val = a / b
        print("나눗셈 결과: {}".format(val))
    except:
        print("예외가 발생했습니다.")
    else:
        print("처리를 정상 종료했습니다.")
    finally:
        print("처리를 종료했습니다.")


print('----- 정상 처리 시 -----')
div_num(4, 2)
print('----- 예외 발생 시 -----')
div_num(10, 0)
