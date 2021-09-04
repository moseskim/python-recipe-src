import matplotlib.pyplot as plt
import numpy as np

# 대상 데이터
x = np.linspace(0, 5, 100)  # x축의 값
y1 = x ** 2
y2 = np.sin(x)

# figure 생성
fig = plt.figure()

# ax를 figure에 설정
ax = fig.add_subplot(1, 1, 1)

# axes에 플롯
ax.plot(x, y1, "-")
ax.plot(x, y2, "-")

# 표시
plt.show()
