import numpy as np

# 계수 행렬
coef = np.array([[3, 1], [1, 3]])

# 상수 행렬
dep = np.array([9, 0])

# 연립 방정식의 해
ans = np.linalg.solve(coef, dep)

# 방정식의 해를 출력
print(ans)

# 검산
c1 = 3 * ans[0] + 1 * ans[1]
c2 = 1 * ans[0] + 3 * ans[1]
print(c1, c2)
