def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    assignments = []
    for p in points:
        min_d = float("inf")
        min_idx = -1
        for (i,c) in enumerate(centroids):
            d = 0
            for k in range(len(c)):
                x = p[k] - c[k]
                d += (x*x)
            if d < min_d:
                min_idx = i
                min_d = d
        assignments.append(min_idx)

    return assignments
    