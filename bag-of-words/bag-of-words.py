import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    token_dict = {}
    vals = []
    for t in tokens:
        if t not in token_dict:
            token_dict[t] = 1
        else:
            token_dict[t] += 1
            
    for v in vocab:
        vals.append(token_dict.get(v,0))
    return np.asarray(vals,dtype=int)
    