import pandas as pd

data = {'height': [161, None, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data)

height_series = df.height

# height 열을 얻어 결손값을 제거한다
new_height_series = height_series.dropna()
print(new_height_series)

# DataFrame에서 결손값이 있는 행을 제거한다
new_df = df.dropna()
print(new_df)
