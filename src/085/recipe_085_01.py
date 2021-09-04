# 클래스 정의
class User:
    """ 사용자 클래스 """

    def __init__(self, name, mail):
        """ 초기화 처리 """
        self.name = name
        self.mail = mail

    def print_user_info(self):
        """ 사용자 정보를 print로 출력 """
        print("사용자 이름: " + self.name)
        print("메일주소: " + self.mail)


# User 타입 객체 생성
user1 = User("User1", "user1@jpub.kr")

# 인스턴스 변수 참조
print(user1.name)

# 메서드 이용
user1.print_user_info()

# 인스턴스 변수 업데이트
user1.mail = "newuser1@jpub.kr"

# 메서드 이용
user1.print_user_info()
