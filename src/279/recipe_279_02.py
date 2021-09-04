import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

# loc릉 이용해 index="Dabin"의 데이터를 얻음
dabin = df.loc["Dabin"]
print(dabin.weight)
