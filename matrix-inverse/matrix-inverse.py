import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A = np.asarray(A)
    if np.ndim(A) != 2:
        return None
    (r,c) = A.shape
    if r != c:
        return None
    if abs(np.linalg.det(A)) < 1e-10:
        return None

    return np.linalg.inv(A)

    