# NumPy (SINGLE DIMENSIONAL ARRAY)
import numpy as np

n1 = np.array([10, 20, 30, 40])
print(n1)
print()
print(type(n1))
print()
import numpy as np

n2 = np.array([[10, 20, 30, 40], [40, 30, 20, 10]])
print(n2)
print()
# numpy with zeros
import numpy as np

n1 = np.zeros((1, 2))
print(n1)
print()
import numpy as np

n1 = np.zeros((5, 5))
print(n1)
print()
# NumPy with same number
import numpy as np

n1 = np.full((2, 2), 10)
print(n1)
print()
# NumPy with arrange
import numpy as np

n1 = np.arange(10, 20)
print(n1)
print()
import numpy as np

n1 = np.arange(10, 50, 5)
print(n1)
print()
# NumPy with random numbers
import numpy as np

n1 = np.random.randint(1, 100, 5)
print(n1)
print()
# NumPy with shapes
import numpy as np

n1 = np.array([[1, 2, 3], [4, 5, 6]])
print(n1.shape)
print()
n1.shape = (3, 2)
print(n1)
print()
# Joining NumPy
import numpy as np

n1 = np.array([10, 20, 30])
n2 = np.array([40, 50, 60])
print(np.vstack((n1, n2)))
print()
print(np.hstack((n1, n2)))
print()
print(np.column_stack((n1, n2)))
print()
import numpy as np

n1 = np.array([10, 20, 30, 40, 50])
n2 = np.array([40, 50, 60, 70, 80])
print(np.intersect1d(n1, n2))
print()
print(np.setdiff1d(n1, n2))
print()
print(np.setdiff1d(n2, n1))
print()
# addition in NumPy (BASIC)
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 + 1
print(n1)
print()
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 - 1
print(n1)
print()
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 * 2
print(n1)
print()
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 / 2
print(n1)
print()
# MEAN
import numpy as np

n1 = np.array([10, 20, 30, 40, 50, 60])
print(np.mean(n1))
print()
# median
import numpy as np

n1 = np.array([11, 44, 5, 96, 67, 85])
print(np.median(n1))
print()
# standard deviation
import numpy as np

n1 = np.array([1, 5, 3, 100, 4, 48])
print(np.std(n1))
print()
# NumPy Matrix
import numpy as np

n1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n1)
print()
print(n1[0])
print()
print(n1[1])
print()
print(n1[:, 1])
print()
print(n1[:, 2])
print()
# numpy matrix transpose
n1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n1)
print()
print(n1.transpose())
print()
# numpy matrix multiplication
n1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n1)
print()
n2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(n2)
print(n1.dot(n2))
print()
print(n2.dot(n1))
print()
# NumPy Save & Load
import numpy as np

n1 = np.array([10, 20, 30, 40, 50, 60])
np.save('my_numpy', n1)
n2 = np.load('my_numpy.npy')
print(n2)
