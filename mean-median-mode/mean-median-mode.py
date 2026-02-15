import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    n = len(x)
    if n == 1:
        return (x[0], x[0], x[0])

    is_odd = n % 2 != 0
    x = np.asarray(x)
    x = np.sort(x)
  
    if is_odd:
        p = (n + 1) / 2
        median = x[int(p)]
    else:
        if n == 2:
          median = (x[0]+x[1])/2
        else:
          p1 = n/2
          p2 = (n/2)+1
          median = (x[int(p1)]+x[int(p2)])/2

    mean = np.sum(x) / n


    mode_dict = Counter(x)
    if mode_dict.most_common()[0][1] == 1:
        mode = None
    else:
        mode = mode_dict.most_common()[0][0]

    return (mean, median, mode)