def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    L = math.sqrt(6/fan_in)
    out = []
    for x in W:
        y = [(a*2*L) -L  for a in x]
        out.append(y)
    return out
