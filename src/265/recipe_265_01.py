import numpy as np

# 기저 벡터 (1, 1, 0)、(0, -1, 0)
a = np.array([[1, 1], [1, -1], [0, 0]])

# QR 분해
q, r = np.linalg.qr(a)
print(q)
print(r)
