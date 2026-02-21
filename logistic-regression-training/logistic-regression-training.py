import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X)
    w = np.zeros(X.shape[1])
    b = 0
    n = X.shape[0]

    for _ in range(steps):
        z = np.dot(X, w) + b
        y_pred = _sigmoid(z)
        err = y_pred - y
        delta_lw = (1/n)*np.dot(X.T, err)
        delta_lb = (1/n)*np.sum(err)
        w = w - lr * delta_lw
        b = b - lr * delta_lb
        
    return (w,b)    