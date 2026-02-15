import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    n = y_pred.shape[0]
    ss = np.sum(np.square(y_pred-y_true))
    return ss/n
