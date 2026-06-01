import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """
    arr = np.array(arr)
    if axis == 0:
        return arr[indices].astype(np.float64)
    elif axis == 1:
        return arr[:,indices].astype(np.float64)
    else:
        return arr
        