import numpy as np


def swap_rows(M, a, b):
    if a < 0 or b < 0 or a >= M.shape[0] or b >= M.shape[0]:
        raise IndexError("Row index out of bounds")
    
    M[[a, b], :] = M[[b, a], :]

def swap_cols(M, a, b):
    if a < 0 or b < 0 or a >= M.shape[1] or b >= M.shape[1]:
        raise IndexError("Column index out of bounds")
    
    M[:, [a, b]] = M[:, [b, a]]



M = np.matrix([[1, 2, 3, 4], 
               [5, 6, 7, 8], 
               [9, 10, 11, 12], 
               [13, 14, 15, 16]])

print("Original Matrix:\n", M)

swap_rows(M, 0, 2)
print("Swapping rows 0 and 2:\n", M)

swap_cols(M, 0, 2)
print("Swapping cols 0 and 2:\n", M)