import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    if norm_type not in ('l2','l1','max'):
        return None

    if axis is not None:
        if axis not in (0,1):
            return None


    matrix = np.asarray(matrix)
    if matrix.ndim != 2:
        return None


    if norm_type == 'l2':
        squares = np.square(matrix)
        sums = np.sum(squares, axis=axis, keepdims=True)
        s = np.sqrt(sums)
        b_safe = np.where(s == 0, 1, s)
        matrix = np.divide(matrix, b_safe)

    if norm_type == 'l1':
        s = np.sum(matrix, axis=axis,keepdims=True)
        b_safe = np.where(s == 0, 1, s)
        matrix = np.divide(matrix, b_safe)

    if norm_type == 'max':
        m = np.max(matrix, axis=axis,keepdims=True)
        b_safe = np.where(m == 0, 1, m)
        matrix = np.divide(matrix, b_safe)
    
    return matrix

