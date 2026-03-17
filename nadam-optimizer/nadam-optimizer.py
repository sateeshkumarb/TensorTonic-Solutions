import numpy as np

def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    # Write code here
    w = np.asarray(w)
    m = np.asarray(m)
    grad = np.asarray(grad)
    v = np.asarray(v)

    m_new = beta1 * m + (1- beta1) * grad
    v_new = beta2 * v + (1- beta2) * np.square(grad)
    num =  beta1 * m_new + (1-beta1) * grad
    val = w  - lr*num/(np.sqrt(v_new) + eps)
    return val, m_new, v_new
    