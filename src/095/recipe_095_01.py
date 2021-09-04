def div_num(a, b):
    try:
        val = a / b
        print(val)
    except TypeError:
        print("연산할 수 없는 인수를 지정했습니다. 처리할 수 없습니다.")
    except ZeroDivisionError:
        print("나눗셈의 분모가 0입니다. 처리할 수 없습니다.")
    except Exception:
        print("알 수 없는 예외가 발생했습니다.")


div_num("abcdefg", 2)
div_num(7, 0)
