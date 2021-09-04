import matplotlib.pyplot as plt

# 데상 데이터
label = ["A", "B", "C", "D", "E"]
x = [40, 30, 15, 10, 5]

# figure 생성
fig = plt.figure()

# ax를 figure로 설정
ax = fig.add_subplot(1, 1, 1)

# axes에 플롯
ax.pie(x, labels=label, counterclock=False, startangle=90)

# 표시 보정
ax.axis('equal')

# 표시
plt.show()
