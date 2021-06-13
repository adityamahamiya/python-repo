# Python Pandas one dimensional labels
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)
print()
print(type(s1))
print()
# changing index
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(s1)
print()
# series objects from dictionary
import pandas as pd

s1 = pd.Series({'a': 10, 'b': 20, 'c': 30})
print(s1)
print()
# changing index
import pandas as pd

print(pd.Series(s1, index=['b', 'c', 'd', 'a']))
print()
# extracting individual elements
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s1[3])
print()
print(s1[:4])
print()
print(s1[-3:])
print()
# adding scalar value to  the series elements
print(s1 + 5)
print()
# adding two series elements
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
s2 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(s1 + s2)
print()
# Pandas data frame
import pandas as pd

df = pd.DataFrame({"Name": ['Bob', 'Sam', 'Anne'], "Marks": [76, 25, 92]})
print(df)
print()
print(type(df))
# data frame in-build function
iris = pd.read_csv('Book1.csv')
print(iris.head())
print()
print(iris.tail())
print()
print(iris.shape)
print()
print(iris.describe())
print()
# .iloc[]
print(iris.iloc[0:3, 0:2])
print()
# .loc[]
print(iris.loc[0:20, ("Item", "Units")])
print()
# dropping columns
print(iris.drop("OrderDate", axis=1))
print()
# dropping rows
print(iris.drop([1, 2, 3], axis=0))
print()
# more functions with Pandas
print("MEAN:-")
print(iris.mean())
print()
print("MEDIAN:-")
print(iris.median())
print()
print("MINIMUM:-")
print(iris.min())
print()
print("MAXIMUM:-")
print(iris.max())
