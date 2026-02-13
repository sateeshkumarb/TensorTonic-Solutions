import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    s = [len(v),len(v)]
    final = np.zeros(s)
    (r, c) = final.shape
    for i in range(r):
        for j in range(c):
            if i==j:
                final[i,j] = v[i]
    return final
