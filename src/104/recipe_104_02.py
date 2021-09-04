enterd = True  # 루프 처리 수행 여부를 나타내는 플래그

while enterd:
    print('키를 입력해 주십시오.')
    c = input()
 
    if c == 'end':
        enterd = False
    else:
        print(c + '을(를) 입력했습니다.')
