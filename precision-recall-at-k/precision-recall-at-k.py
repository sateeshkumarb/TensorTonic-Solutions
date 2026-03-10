def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    rl = len(relevant)
    k_recs = recommended[:k]
    relevant = set(relevant)
    hits = 0
    for r in k_recs:
        if r in relevant:
            hits += 1
    if hits == 0:
        return [0.0, 0.0]
    return [hits/k, hits/rl]
    