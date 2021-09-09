import matplotlib.pyplot as plt

# 1. figure 생성
fig = plt.figure()

# 2. 생성한 figure에 axes를 생성하고 배치
ax1 = fig.add_subplot(1, 1, 1)

# 3. axes에 그림 데이터 설정
X = [0, 1, 2]
Y = [0, 1, 2]
ax1.plot(X, Y)

# 4. 표시
plt.show()
