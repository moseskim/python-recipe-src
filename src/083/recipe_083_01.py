def sample_generator():
    """ 제너레이터 함수 """
    print("처리 시작")
    yield 'Good morning'
    print("처리 재개")
    yield 'Good afternoon'
    print("처리 재개")
    yield 'Good night'


gen_obj = sample_generator()  # 제너레이터 객체를 생성한다
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
