import numpy as np

# 배열 생성(dtype 미지정)
x1 = np.array([1, 2, 3])
print(x1.dtype)

# 배열 생성(dtype에 float64 지정)
x2 = np.array([1, 2, 3], dtype=np.float64)
print(x2.dtype)