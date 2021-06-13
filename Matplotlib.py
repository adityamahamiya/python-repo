# Line Plot
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
print(x)
print()
y = 2 * x
print(y)
print()
plt.plot(x, y)
plt.show()
print()
# Line Plot - 2 (adding titles and labels)
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()
print()
# Line Plot - changing line aesthetics
plt.plot(x, y, color='red', linestyle=':', linewidth=2)
plt.show()
print()
# Line Plot - two lines
x = np.arange(1, 11)
y1 = 2 * x
y2 = 3 * x
plt.plot(x, y1, color='red', linestyle=':', linewidth=2)
plt.plot(x, y2, color='green', linestyle='-', linewidth=3)
plt.title("Line Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.grid(True)
plt.show()
# Line Plot - adding subplots
x = np.arange(1, 11)
y1 = 2 * x
y2 = 3 * x
plt.subplot(1, 2, 1)
plt.plot(x, y1, color='red', linestyle=':', linewidth=2)
plt.subplot(1, 2, 2)
plt.plot(x, y2, color='green', linestyle=':', linewidth=3)
plt.show()
# Bar plot
student = {"Bob": 87, "Matt": 56, "Sam": 27}
names = list(student.keys())
values = list(student.values())
plt.bar(names, values)
plt.show()
# bar plot adding labels and grid
plt.bar(names, values)
plt.title("Marks of  Students")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.grid(True)
plt.show()
# horizontal bar plot
plt.barh(names, values, color='orange')
plt.title("Marks of  Students")
plt.xlabel("Marks")
plt.ylabel("Names")
plt.grid(True)
plt.show()
# Scalar plot
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = [8, 1, 7, 2, 0, 3, 5, 3, 4]
plt.scatter(x, a)
plt.show()
# Scalar plot - 2
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = [8, 1, 7, 2, 0, 3, 5, 3, 4]
plt.scatter(x, a, marker="*", c="g", s=100)
plt.show()
# Scalar plot - 3
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = [8, 1, 7, 2, 0, 3, 5, 3, 4]
b = [4, 3, 5, 3, 0, 2, 7, 1, 8]
plt.scatter(x, a, marker="*", c="red", s=100)
plt.scatter(x, b, marker=".", c="yellow", s=150)
plt.show()
# Scalar plot - 4
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = [8, 1, 7, 2, 0, 3, 5, 3, 4]
b = [4, 3, 5, 3, 0, 2, 7, 1, 8]
plt.subplot(1, 2, 1)
plt.scatter(x, a, marker="*", c="red", s=100)
plt.subplot(1, 2, 2)
plt.scatter(x, b, marker=".", c="yellow", s=150)
plt.show()
# Histogram
data=[1,3,3,3,3,3,9,9,5,4,4,8,8,8,6,7]
plt.hist(data)
plt.show()
# Histogram - 2
plt.hist(data,color="g",bins=4)
plt.show()
# Histogram -3 dataset
import pandas as pd
iris=pd.read_csv('Book1.csv')
iris.head()
plt.hist(iris['Units'],bins=30,color="r")
plt.show()
