import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)
print(df)

# loc를 이용해 index="Dabin"의 데이터를 얻음
dabin = df.loc["Dabin"]
print(dabin)

# iloc를 이용해 index=3의 데이터를 얻음
maru = df.iloc[3]
print(maru)
