import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    X = np.asarray(X)
    labels = np.asarray(labels)
    ks = np.unique(labels)
    sil_score = 0.0
    for k in ks:
        intra_cluster = X[labels == k]
        for p in intra_cluster:
            norm_a = np.linalg.norm(intra_cluster - p, axis=1)
            picks = np.nonzero(norm_a) # mean will be zero for the same point, so exclude it
            a = np.mean(norm_a[picks])

            min_b = np.inf
            for j in [x for x in ks if x != k]:
                outside_cluster = X[labels == j]
                norm_b = np.linalg.norm(outside_cluster - p, axis=1)
                b = np.mean(norm_b)
                if b < min_b:
                    min_b = b
            si = (min_b-a)/max(a,min_b)            
            sil_score += si


    return sil_score/len(X)
    
