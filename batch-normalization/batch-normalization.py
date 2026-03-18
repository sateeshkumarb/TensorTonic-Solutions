import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.asarray(x)
    gamma = np.asarray(gamma)
    beta = np.asarray(beta)
    if x.ndim == 4:
        mu_x = np.mean(x, axis=(0,2,3), keepdims=True)
        var_x = np.var(x, axis=(0,2,3), keepdims=True)
        res = (1,-1,1,1)
        gamma = np.reshape(gamma,(res))
        beta = np.reshape(beta, (res))
    else:
        mu_x = np.mean(x, axis=0, keepdims=True)
        var_x = np.var(x, axis=0, keepdims=True)

    x_i = (x-mu_x)/np.sqrt(var_x+eps)
    y = gamma*x_i + beta
    return y
    

    