class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def __str__(self):
        return "사용자명: " + self.name + ", 메일주소: " + self.mail

    def __repr__(self):
        return str({'name': self.name, 'age': self.mail})


user = User("User1", "user1@example.com")
print(user)
print(repr(user))
