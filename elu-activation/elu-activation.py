import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = np.asarray(x)
    return np.where(x>0,x,alpha*(np.exp(x)-1)).tolist()