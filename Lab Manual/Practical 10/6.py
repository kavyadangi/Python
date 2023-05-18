import numpy as np
import pandas as pd
df = pd.DataFrame({'A': [1, 2, np.nan, 4, np.nan], 'B': [5, np.nan, np.nan, 8, 9], 'C': [10, 11, 12, 13, 14], 'D': [np.nan, np.nan, np.nan, np.nan, np.nan]})
print("Original DataFrame:")
print(df)
df.fillna("No Value", inplace=True)
print("\nDataFrame after replacing missing values:")
print(df)
