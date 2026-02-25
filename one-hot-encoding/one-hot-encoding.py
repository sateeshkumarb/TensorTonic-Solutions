import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    if num_classes is not None:
        dim = num_classes
    else:
        dim = len(np.unique(y))
    oh = np.eye(dim)[y]
    
    return oh    