def div_num(a, b):
    try:
        val = a / b
        print(val)
    except Exception as e:
        print("예외가 발생했습니다. 호출 측에서 처리하십시오.")
        raise e


div_num(7, 0)
