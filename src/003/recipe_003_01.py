def main():
    """
    큰따옴표 3개를 사용하면 docstring이 된다.
    여기에 함수의 설명을 입력
    """

    # 보통 주석은 #을 이용한다.
    # 일반문과 같이 들여쓰기를 포함해야 한다.
    print("hello world!")

    # if문에서는 들여쓰기를 한다.
    x = 100
    if x > 100:
        print("x는 100보다 큽니다.")

    # 루프에서도 들여쓰기를 한다.
    num_list = [0, 1, 3]
    for num in num_list:
        # 블록 내부에서는 주석도 들여쓰기를 한다.
        print(num)

        # 코드가 중접되면 그만큼 들여쓰기를 추가한다.
        if num > 1:
            print("num은 1보다 큽니다.")

    # pass는 아무것도 하지 않는 구문
    pass

    # 들여쓰기 내부에서 아무 처리도 하지 않을 때는 pass를 기술한다.
    if x < 100:
        pass

    # 긴 문장은 중간에 \를 써서 개행할 수 있다.
    y = 1 + 2 + 3 + 4 + 5 \
    + 6 + 7 + 8 + 9 + 10
    print(y)


if __name__ == "__main__":
    main()  # main 함수 호출
