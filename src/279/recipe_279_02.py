import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
# name = ["Yamada", "Suzuki", "Sato", "Tanaka", "Watanabe"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

# at을 이용한 업데이트
df.at['Dabin', 'weight'] = 77
print(df)
