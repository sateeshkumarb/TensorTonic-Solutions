import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    np.random.seed(seed)
    # rng = np.random.default_rng(seed=seed)
    if kind == "uniform":        
        return np.random.random(shape)
        # return rng.uniform(size=shape).astype(np.float64)
    elif kind == "normal":
        return np.random.standard_normal(shape)        
        # return rng.standard_normal(size=shape).astype(np.float64)
    
