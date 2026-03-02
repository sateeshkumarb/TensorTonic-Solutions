import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    y_all = np.r_[y_left, y_right]    
    n = len(y_all)
    if n == 0:
        return 0.0
        
    n_l = len(y_left)/n
    n_r = len(y_right)/n
    print(f"n_l:{n_l},n_r:{n_r}")

    def gini(y):
        if y is None or len(y) == 0:
            return 0
        uqs, counts = np.unique(y, return_counts=True)
        if uqs.size == 1:
            return 0

        total = np.sum(counts)
        
        if total == 0:
            return 0
            
        sum_ps = 0.0
        for c in counts:
            p = c / total
            sum_ps += p * p
        return (1- sum_ps)
    g_all = n_l*gini(y_left)+n_r*gini(y_right)
    return n_l*gini(y_left)+n_r*gini(y_right)    
        
