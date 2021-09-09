import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

s = [171, 178, 183, 179, 198]
df["height"] = pd.Series(s, index=name)
print(df)
