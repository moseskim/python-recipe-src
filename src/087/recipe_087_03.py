class Sample():
    class_val1 = 1
    class_val2 = 2

    def __init__(self):
        pass


Sample.class_val2 = 999

s = Sample()

# 클래스 변수를 참조할 수 있다
print(s.class_val1, s.class_val2)

# 대입을 시도한다
s.class_val1 = 100

# 새롭게 인스턴스 변수 class_val1이 설정된다
print(s.class_val1, Sample.class_val1)
