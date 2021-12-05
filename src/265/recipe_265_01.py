import numpy as np

a = np.array([[1, 3], [2, -1]])

# 행렬 표시
print(a)

# 전치 행렬
print(a.T)

# 트레이스
print(a.trace())

# 역행렬
print(np.linalg.inv(a))

# 행렬식
print(np.linalg.det(a))

# 순위
print(np.linalg.matrix_rank(a))
