import matplotlib.pyplot as plt

# 대상 데이터
x = [1, 2, 3, 4, 5]

y1 = [100, 300, 200, 500, 0]
y2 = [150, 350, 250, 550, 50]
y3 = [200, 400, 300, 600, 100]
y4 = [250, 450, 350, 650, 150]

# figure 생성
fig = plt.figure()

# ax를 figure에 설정
ax = fig.add_subplot(1, 1, 1)

# axes에 plot
ax.plot(x, y1, "-", c="#ff0000", linewidth=1, marker='*', alpha=1)
ax.plot(x, y2, "--", c="#00ff00", linewidth=2, marker='o', alpha=0.5)
ax.plot(x, y3, "-.", c="#0000ff", linewidth=4, marker='D', alpha=0.5)
ax.plot(x, y4, ":", c="#ff00ff", linewidth=4, marker='x', alpha=0.5)

# 표시
plt.show()
