import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    ts_X = X.T@X
    inv_X = np.linalg.inv(ts_X)
    return inv_X@X.T@y