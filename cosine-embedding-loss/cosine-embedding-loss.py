import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    x1_mag = np.sqrt(np.dot(x1,x1))
    x2_mag = np.sqrt(np.dot(x2,x2))
    x1_norm = x1/x1_mag
    x2_norm = x2/x2_mag
    x1_mag_norm = np.sqrt(np.dot(x1_norm,x1_norm))
    x2_mag_norm = np.sqrt(np.dot(x2_norm,x2_norm))
    x12_dot = np.dot(x1_norm,x2_norm)
    cos = x12_dot/x1_mag_norm*x2_mag_norm
    cos = np.clip(cos,-1,1)
    if label == 1:
        loss = 1 - cos
    else:
        loss = max(0,(cos-margin))

    return loss
    
