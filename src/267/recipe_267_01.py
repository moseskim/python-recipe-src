import numpy as np

a = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
w, v = np.linalg.eig(a)

# 고유값
print(w)

# 고유 벡터
print(v)
