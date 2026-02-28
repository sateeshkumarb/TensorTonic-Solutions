import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    if not isinstance(matrix, list):
        return None
    if not matrix:
        return None 
        
    vals = [isinstance(x, list) and len(x) for x in matrix]
    
    if not all(vals):
        return None

    prev = vals[0]
    if len(vals) > 0:
        for v in vals[1:]:
            if prev != v:
                return None
            prev = v

    r, c = np.shape(matrix)

    if r != c:
        return None # not a square matrix
        
    evs = np.linalg.eigvals(matrix)
    return evs