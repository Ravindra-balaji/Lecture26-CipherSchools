# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HMqzyKKsqJYfYuoi0yx86oj9-Dmj_dfc
"""

# Loading the dataset

import pandas as pd

df = pd.read_csv("Diabetes Missing Data.csv")
print(df)

# Identify missing values
print(df.isnull().sum())

df.info()

# Removing rows with Missing Values

df_cleaned = df.dropna()
print(df_cleaned)

"""# Filling Missing Values


"""

# Fill missing values with a specific value

df_filled = df.fillna({
    'Glucose' : df['Glucose'].mean(),
    'Skin_Fold' : 11
})
print(df_filled)

"""#  Forward fill method"""

df_ffil = df.fillna(method = "ffill") #"bfill for backward fill"
print(df_ffil)

"""# Removing Duplicates"""

# Add duplicate row for demonstration
df = pd.concat([df, df.iloc[[0]], df.iloc[[1]]], ignore_index=True)
print("Before removing duplicates:\n",df)

df_no_duplicates = df.drop_duplicates()
print("After removing duplicates:\n",df_no_duplicates)

"""# Replacing Incorrect Values"""

# Replace incorrect values in 'Age' column
df_corrected = df.replace({'Age' : {50 : 90, 31 : 30}})
print(df_corrected)

"""# Ensuring Consistency"""

# Convert all department names to lowercase for consistency
df['Serum_Insulin'] = df['Serum_Insulin'].str.lower()
print(df)

"""# Normalization"""

df_normalized = df.copy()
for col in ['Age', 'Pregnant']:
  df_normalized[col] = (df[col] - df[col].min())/ (df[col].max() - df[col].min())

# Print original and normalized values
print("Original DataFrame:")
print(df)
print("\nNormalized DataFrame:")
print(df_normalized)