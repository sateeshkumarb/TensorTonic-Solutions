def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    maxs = []
    mins  = []
    
    for j in zip(*data):
        maxs.append(max(j))
        mins.append(min(j))

    for i,d in enumerate(data):
        for j,v in enumerate(d):
            if maxs[j] == mins[j]:
                data[i][j] = 0
            else:
                data[i][j] = (data[i][j]-mins[j])/(maxs[j]-mins[j])
    return data
