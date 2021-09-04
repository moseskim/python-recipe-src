import matplotlib.pyplot as plt

# figure 생성
fig1 = plt.figure()

# 그래프 그림 설정
ax = fig1.add_subplot(1, 1, 1)
x1 = [-2, 0, 2]
y1 = [-2, 0, 2]
ax.plot(x1, y1)

x2 = [-2, 0, 2]
y2 = [-4, 0, 4]
ax.plot(x2, y2)

ax.grid(True)  # grid 표시 ON
ax.set_xlim(left=-2, right=2)  # x축 범위
ax.set_ylim(bottom=-2, top=2)  # y축 범위
ax.set_xlabel('x')  # x축 라벨
ax.set_ylabel('y')  # y축 라벨
ax.set_title('ax title')  # 그래프 타이틀
ax.legend(['f(x)=x', 'g(x)=2x'])  # 범례 표시
plt.show()
