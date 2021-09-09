import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

# height 열을 []로 얻음
height = df["height"]
print(height)

# weight 열을 .으로 얻음
weight = df.weight
print(weight)
