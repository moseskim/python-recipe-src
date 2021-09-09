from matplotlib import pyplot

# 플롯할 점
X = [1, 2, 3]
Y = [1, 1, 1]

# 함수를 호출해서 플롯
pyplot.scatter(X, Y, c='b', label='test_data')

# 함수를 호출해서 범례 설정
pyplot.legend(['test1'])

# 함수를 호출해서 제목 설정
pyplot.title("sample1")

# 표시
pyplot.show()
