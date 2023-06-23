import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
c = a + b
print(c)
# Output: [5 7 9]

# Element-wise multiplication
d = a * b
print(d)
# Output: [4 10 18]

# Matrix multiplication
e = np.dot(a, b)
print(e)
# Output: 32

# Mathematical functions
f = np.sin(a)
print(f)
# Output: [0.84147098 0.90929743 0.14112001]
