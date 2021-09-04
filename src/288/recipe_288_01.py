import matplotlib.pyplot as plt

# 플롯할 점
X = [1, 2, 3]
Y = [1, 1, 1]

# figure 객체를 생성
fig = plt.figure()

# axes 객체를 figure 객체에 설정
ax = fig.add_subplot(1, 1, 1)

# axes 객체에 산포도 설정
ax.scatter(X, Y, color='b', label='test_data')

# axes 객체제 범례 설정
ax.legend(["test1"])

# axes 객체에 제목 설정
ax.set_title("sample1")

# 표시
plt.show()
