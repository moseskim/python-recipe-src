class Sample1():
    """ 수퍼 클래스 """
    pass


class Sample2(Sample1):
    """ Sample1의 서브 클래스 """
    pass


obj1 = Sample1()  # Sample1 타입 객체를 생성한다
obj2 = Sample2()  # Sample2 타입 객체를 생성한다

print(" ----- isinstance를 이용한 비교 결과 ----- ")
print(isinstance(obj1, Sample1))  # True
print(isinstance(obj1, Sample2))  # False
print(isinstance(obj2, Sample1))  # True
print(isinstance(obj2, Sample2))  # True

print(" ----- Type 결과 비교 ----- ")
print(type(obj1) == Sample1)  # True
print(type(obj1) == Sample2)  # False
print(type(obj2) == Sample1)  # False
print(type(obj2) == Sample2)  # True
