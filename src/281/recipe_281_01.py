import pandas as pd

name = ["Garam", "Nagil", "Dabin", "Maru", "Bada"]
score1 = {'korean': [55, 81, 73, 63, 88], 'math': [95, 80, 99, 79, 77]}
score2 = {'korean': [65, 74, 75, 59, 58], 'math': [97, 69, 72, 83, 66]}
df1 = pd.DataFrame(score1, index=name)
df2 = pd.DataFrame(score2, index=name)

sum_df = df1 + df2
print(sum_df)
