def main():
    """
    큰 따옴표 3개를 사용하면 docstring이 됩니다.
    여기에 함수의 설명을 입력합니다.
    """

    # 보통 주석은 #을 이용합니다.
    # 일반문과 같이 들여쓰기를 포함해야 합니다.
    print("hello world!")

    # if문에서는 들여쓰기를 합니다.
    x = 100
    if x > 100:
        print("x는 100보다 큽니다.")

    # 루프에서도 들여쓰기를 합니다.
    num_list = [0, 1, 3]
    for num in num_list:
        # 블록 내부에서는 주석도 들여쓰기를 합니다.
        print(num)

        # 코드가 중접되면 그만큼 들여쓰기를 추가합니다.
        if num > 1:
            print("num은 1보다 큽니다.")

    # pass는 아무것도 하지 않는 구문입니다.
    pass

    # 들여쓰기 내부에서 아무 처리도 하지 않을 때는 pass를 기술합니다.
    if x < 100:
        pass


if __name__ == "__main__":
    main()  # main 함수 호출
