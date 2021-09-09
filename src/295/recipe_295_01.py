import matplotlib.pyplot as plt
import numpy as np

# 대상 데이터
x = np.random.normal(0, 10, 1000)

# figure 생성
fig = plt.figure()

# ax를 figure로 설정
ax = fig.add_subplot(1, 1, 1)

# axes에 플롯
ax.hist(x, bins=10, color="#00AAFF", ec="#0000FF", alpha=0.5)

# 표시
plt.show()
