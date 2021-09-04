def div_num(a, b):
    try:
        val = a / b
        print(val)
    except ZeroDivisionError:
        print("나눗셈의 분모가 0이므로 처리할 수 없습니다.")


div_num(8, 2)
div_num(7, 0)
div_num(5, 2)
