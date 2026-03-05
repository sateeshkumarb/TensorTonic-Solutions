def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    outs = []
    for i in values:
        xs = [i**t for t in range(degree+1)]
        outs.append(xs)
        
    return outs
    