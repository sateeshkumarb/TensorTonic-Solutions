import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    x1_mag = np.sqrt(np.dot(x1, x1))
    x2_mag = np.sqrt(np.dot(x2, x2))
    cos = np.dot(x1, x2) / (x1_mag * x2_mag)
    if label == 1:
        loss = 1 - np.dot(x1, x2) / (x1_mag * x2_mag)
    else:
        loss = max(0, (cos - margin))
    return loss    
