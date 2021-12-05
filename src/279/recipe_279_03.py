import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

mod_garam = pd.Series([171, 66], index=["height", "weight"])
df.loc["Garam"] = mod_garam
print(df)
