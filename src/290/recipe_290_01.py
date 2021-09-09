from matplotlib import pyplot as plt
import numpy as np

# 무작위로 점을 생성
x = np.random.rand(50)
y = np.random.rand(50)

# figure 생성
fig = plt.figure()

# ax를 figure에 설정
ax = fig.add_subplot(1, 1, 1)

# 플롯 마커 크기, 색상, 투명도 설정
ax.scatter(x, y, s=300, alpha=0.5, linewidths=2, marker='*', c='#aaaaFF', edgecolors='blue')
plt.show()
