import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    w = np.asarray(w)
    grad = np.asarray(grad)
    m = np.asarray(m)
    v = np.asarray(v)
    m_new = beta1 * m + (1- beta1) * grad
    v_new = beta2 * v + (1- beta2) * np.square(grad)
    dr = np.sqrt(v_new) + eps
    w_new = w - (weight_decay* lr * w) - lr * (m_new/dr)
    return w_new,m_new,v_new    
    