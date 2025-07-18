import numpy as np

vec = np.array([2, 2, 4])

e0 = np.array([1, 0, 0])
e1 = np.array([0, 1, 0])
e2 = np.array([0, 0, 1])

print("e0:", np.dot(vec, e0))
print("e1:", np.dot(vec, e1))
print("e2:", np.dot(vec, e2))


