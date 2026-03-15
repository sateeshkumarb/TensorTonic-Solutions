import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param = np.asarray(param)
    grad = np.asarray(grad)
    m=np.asarray(m)
    v= np.asarray(v)
    
    m_new = beta1 * m + (1- beta1) * grad
    v_new = beta2 * v + (1- beta2) * np.square(grad)
    m_t = m_new/(1-np.pow(beta1,t))
    v_t = v_new/(1-np.pow(beta2,t))
    dr = np.sqrt(v_t)+eps
    param_new = param - lr * (m_t/dr)
    return (param_new,m_new,v_new)
    