import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y)
    _,cs = np.unique(y,return_counts=True)
    ratios = cs/np.sum(cs)
    logs = -1*ratios*np.log2(ratios)
    return np.sum(logs)
    