class User:
    """ 사용자 클래스 """

    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def print_user_info(self):
        print("사용자 이름: " + self.name)
        print("메일주소: " + self.mail)


class StudentUser(User):
    def __init__(self, name, mail, grade):
        super().__init__(name, mail)
        self.grade = grade

    def answer_question(self):
        print("문제에 대답합니다.")

    def print_grade(self):
        print(str(self.grade) + "학년입니다.")


# StudentUser 객체 생성
student = StudentUser("Student1", "student1@example.com", 3)

# User의 메서드 실행
student.print_user_info()

# StudentUser의 메서드 실행
student.answer_question()
student.print_grade()
