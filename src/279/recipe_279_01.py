import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

# at
dabin_weight = df.at['Dabin', 'weight']
print(dabin_weight)

# iat
maru_height = df.iat[3, 1]
print(maru_height)
