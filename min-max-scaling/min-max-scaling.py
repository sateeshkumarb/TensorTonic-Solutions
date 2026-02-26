def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    cols = list()
    d = data[0]
    for j in range(len(d)):
        cols.append([])

    for d in data:
        for j,v in enumerate(d):
            cols[j].append(v)
    maxs =[max(x) for x in cols]
    mins = [min(x) for x in cols]

    for i,d in enumerate(data):
        for j,v in enumerate(d):
            if maxs[j] == mins[j]:
                data[i][j] = 0
            else:
                data[i][j] = (data[i][j]-mins[j])/(maxs[j]-mins[j])
    return data
