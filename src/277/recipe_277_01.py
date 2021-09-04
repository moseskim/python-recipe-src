import pandas as pd

data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data)

# 평균값 산출
m = df.mean()

print(m)

# 각 열의 평균값 참조
print(m.height)
print(m.weight)
