def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    if len(assignments) == 1:
        return points

    mapping = {}
    for key,v in zip(assignments,points):
        mapping.setdefault(key,[]).append(v)
    mlen = max([len(v[0]) for v in mapping.values() if v])
    for i in range(k):
        if mapping.get(i) is None:
            mapping[i] = []
    

    new_centroids = []
    for i in range(k):
        means = [0]*mlen
        if mapping[i]:
            r = len(mapping[i][0])
        else:
            r = 0
        for j in range(r):
            zeros = [x[j] for x in mapping[i]]
            means[j]= sum(zeros)/len(zeros)
        new_centroids.append(means)

    return new_centroids    
