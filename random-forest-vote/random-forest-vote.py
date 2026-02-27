import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    choices = []
    preds = zip(*predictions)
    for p in preds:
        preds,counts = np.unique(p,return_counts=True)
        count_matrix = {}
        for pred,count in zip(preds,counts):
            count_matrix[int(pred)] = int(count)
        max_cnt = -1
        idx = 0
        for k in sorted(count_matrix.keys()):
            v = count_matrix[k]
            if v > max_cnt:
                max_cnt = v
                idx = k
        choices.append(idx)
    return choices
    
    