import numpy as np

def set_array(L, rows, cols, col_order = False):
    if len(L) != rows * cols:
        raise ValueError("Length of list does not match specified dimensions.")
    
    mat = np.zeros((rows, cols))

    count = 0
    if col_order:
        for j in range(cols):
            for i in range(rows):
                mat[i, j] = L[count]
                count += 1
    else:
        for i in range(rows):
            for j in range(cols):
                mat[i, j] = L[count]
                count += 1

    return mat


print(set_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 4))