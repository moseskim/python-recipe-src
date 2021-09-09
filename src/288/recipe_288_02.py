import matplotlib.pyplot as plt

# figure 생성
fig = plt.figure()

# 2x3의 1번째
ax1 = fig.add_subplot(2, 3, 1)
ax1.set_title('1')  # 그래프 제목
# 2x3의 2번째
ax2 = fig.add_subplot(2, 3, 2)
ax2.set_title('2')  # 그래프 제목
# 2x3의 3번째
ax3 = fig.add_subplot(2, 3, 3)
ax3.set_title('3')  # 그래프 제목
# 2x3의 4번째
ax4 = fig.add_subplot(2, 3, 4)
ax4.set_title('4')  # 그래프 제목
# 2x3의 5번째
ax5 = fig.add_subplot(2, 3, 5)
ax5.set_title('5')  # 그래프 제목
# 2x3의 6번째
ax6 = fig.add_subplot(2, 3, 6)
ax6.set_title('6')  # 그래프 제목

# 표시
plt.show()
