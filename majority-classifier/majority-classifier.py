import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    (vals,counts) = np.unique(y_train,return_counts=True)
    if np.all(counts == counts[0]):
        return np.full_like(X_test, y_train[0])
    else:
        idx = counts.argmax()
        return np.full_like(X_test, vals[idx])