import matplotlib.pyplot as plt

# 레이블
label = ['A', 'B', 'C', 'D', 'E']

# 대상 데이터
x = [1, 2, 3, 4, 5] # 가로축
height = [3, 5, 1, 2, 3] # 값

# figure 생성
fig = plt.figure()

# ax를 figure에 설정
ax = fig.add_subplot(1, 1, 1)

# axes에 막대그래프 설정
ax.bar(x, height, label=label, linewidth=1, edgecolor="#000000")

# 표시
plt.show()
