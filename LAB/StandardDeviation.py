import math
import numpy as np


def mean(x):
    return sum(x) / n


def sd(x):
    Sum = 0
    avg = mean(x)
    for i in x:
        Sum += (i - avg) ** 2
    return math.sqrt(Sum / (n - 1))


n = int(input("Enter total number of elements : "))
print("Enter values")
x = [int(x) for x in input().split(",")]
print("Standard Deviation : ", sd(x))

print(np.std(x))
