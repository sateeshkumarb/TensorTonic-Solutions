import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    diffs = np.abs(y_true - y_pred)
    use_mse = np.where(diffs <= delta, 0.5 * np.square(diffs), 0)
    use_mae = np.where(diffs > delta, delta * diffs - 0.5 * np.square(delta), 0)
    return np.mean(use_mse+use_mae)
