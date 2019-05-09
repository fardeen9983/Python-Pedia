"""
Numpy is used for statistical operations in python
It is one of the most popular python libraries
Deals with n dimensional vectors (arrays)

Advantages:
1. Extension to Python of multi dimensional arrays
2. Hardware efficient
3. Designed for scientific computuation
"""

import numpy as np

# Create a numpy array (vector)
a = np.array([0, 1, 2, 3, 4, 5])
print(a)

# Print the type of values the array holds
print("Data type ", a.dtype)

# Create a numpy array from 0..to n
a = np.arange(10)
print(a)

# To create an arange array of specific data type
a = np.arange(10, dtype="double")
print("Double array", a)
# 0. -> 0.0

# Create an array using arange with start (inclusive) and end (exclusive) value and step size
a = np.arange(1, 10, 2)
print(a)

# Create an array raised to some power
a2 = a ** 2
print(a2)

# Get the dimension of the np array
print(a.ndim)

# 2-D array (Matrix)
b = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(b)

# Fetch the shape of np array
print(b.shape)  # (a,b) a rows and b columns
print(a.shape)  # (a,) a elements

# 3-D arrays (Tensor)
c = np.array([[[1, 2], [2, 3]], [[3, 4], [4, 5]], [[5, 6], [6, 7]]])
print(c, "\n", c.ndim, "\n", c.shape)

"""
Create vector using link space 
method : linspace
arg0 : start value
arg1 : end value 
Both inclusive
arg3 : Total number of values
"""
a = np.linspace(1, 10, 25)
print(a)

# Create an one matrix/ multi dimensional array
a = np.ones((3, 3))  # 3x3 one matrix
print(a)

a = np.ones((2, 3, 4))  # 2x3x4 one matrix
print(a)

# Create a 0 value matrix. Always create decimal point values
a = np.zeros((3, 3))  # 3x3 zero matrix
print(a)

a = np.zeros((2, 3, 4))  # 2x3x4 zero matrix
print(a)

# Create an identity matrix
a = np.eye(3)  # 3x3 zero matrix
print(a)

# Create diagonal arrays
a = np.diag([1, 2, 3, 4])
print(a)

# Fetch diagonal values from a diagonal array in the form of a vector
print(np.diag(a))  # a is a diagonal matrix

# Create a random array of given shape
# THis will generate a vector of 4 uniformly     distributed random no
print("Random vector : ", np.random.rand(5))

print("Random Integer vector : ", np.random.randint(0, 10, 5))

print("Random matrix : ", np.random.rand(2, 3))

# Standard normal variant / caution distributed random no
print("Random vector : ", np.random.randn(5))

# Create array of complex numbers (complex128)
c = np.array([2 + 1j, 9.0 + 4.5j])
print("Complex array : ", c, c.dtype)

# Boolean array (bool)
b = np.array([True, False, False, False, True])
print("Boolean array : ", b, b.dtype)

# String array
s = np.array(["Hey", "how", "are", "you"])
print("String array : ", s, s.dtype)

"""
Indexing in numpy arrays
We can manipulate and access numpy array elements through indexes the same way we do with normal arrays
Also the indexes start from 0 to length-1 
"""

# A random array
a = np.random.rand(5)
print("5th element : ", a[4])

# A 2D array
a = np.diag([1, 2, 3, 4])
print("Element at 3nd row and 3rd column : ", a[2, 2])

# Assigning values by index
a[2, 2] = 4
print("Element at 3nd row and 3rd column : ", a[2, 2])
