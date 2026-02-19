import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.asarray(x)
    erfx = np.vectorize(math.erf)(x/math.sqrt(2))
    return np.multiply(x/2, 1 + erfx)
