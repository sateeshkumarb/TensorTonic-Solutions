import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if len(x)!=len(p):
      raise ValueError("size mismatch")
    x = np.asarray(x)
    p = np.asarray(p)
    if np.sum(p) > 1.0:
      raise ValueError("wrong probs")
    if np.sum(p) < 1.0:
      raise ValueError("invalid probs")
    return np.sum(np.multiply(x,p))
