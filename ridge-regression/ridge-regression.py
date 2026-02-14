def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.asarray(X)
    y = np.asarray(y)
    ts_X = X.T@X
    id_matrix = np.identity(ts_X.shape[0])
    inv_X = np.linalg.inv(ts_X+lam*id_matrix)
    ridge = inv_X@X.T@y
    return ridge
    