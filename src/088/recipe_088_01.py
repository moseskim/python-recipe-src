class Sample():
    class_val1 = 1

    def __init__(self, val1):
        self.instance_val1 = val1

    def instance_method(self):
        print(self.class_val1, self.instance_val1)

    @classmethod
    def class_method(cls):
        print(cls.class_val1)

    @staticmethod
    def static_method():
        local_val = 100
        print(local_val)


# 인스턴스 메서드 호출
s = Sample(10)
s.instance_method()
# 클래스 메서드 호출
Sample.class_method()
# 스태틱 메서드 호출
Sample.static_method()
