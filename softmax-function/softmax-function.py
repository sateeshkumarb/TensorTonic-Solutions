import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x)
    if x.ndim == 1:
        axis = None
    else:
        axis = 1
    max = np.max(x,axis=axis,keepdims=True)
    ex = np.exp(x-max)
    s = np.sum(ex,axis=axis,keepdims=True)
    k = ex/s
    return k    