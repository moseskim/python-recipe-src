import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 위 코드에서 계속
s["c"] = 100
s.d = 200
print(s)
