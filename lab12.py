import pandas as pd
import numpy as np

df = pd.read_csv('lab12_flat_file.csv')

# gender
df['gender'].value_counts()

df['gender'].replace('Male', 'male', inplace = True)

df['gender'].fillna(value = 'female', inplace = True)

# hair_color
df['hair_color'].value_counts()

df['hair_color'].fillna(value = 'brown', inplace = True)

# eye_color
df['eye_color'].value_counts()

df['eye_color'].fillna(value = 'brown', inplace = True)

# height
print(df.height)
df['height'].fillna(df.height.mean, inplace = True)

# is the missing data gone?
df.isnull().sum()
# yes

# part two
df.mean()
df['height'].sum()
df.median()
df.mode()
df.describe()

df['gender'].mode()
df['hair_color'].mode()
df['eye_color'].mode()