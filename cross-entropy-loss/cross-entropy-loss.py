import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    k = len(np.unique(y_true))
    
    if k == 1:
        picks = y_pred[:,y_true]
    else:
        y_true_one_hot = np.eye(k)[y_true]
        col_indicies = np.argmax(y_true_one_hot,axis=1)
        n = y_pred.shape[0]
        row_indicies = np.arange(n)
        picks = y_pred[np.arange(n),col_indicies]
        
    log_picks = -1*np.log(picks)
    ce = np.mean(log_picks)
    return ce
    