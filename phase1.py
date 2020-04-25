# Import necessary packages
import pandas as pd
import numpy  as np

# Reading Data
timedf = pd.read_csv('PrepSiteTimeMatrix.csv', nrows=41, dtype={0:int}, header=0, index_col=0)

print(timedf.axes[0].tolist())
first = timedf.axes[0].tolist()[0]
print(timedf.loc[first])

print(type(first))

# Regular py file

ls = []
ls.append(3)
print(ls.pop())
