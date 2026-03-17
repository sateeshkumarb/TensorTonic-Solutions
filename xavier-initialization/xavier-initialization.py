def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    L = math.sqrt(6/(fan_in+fan_out))
    out = []
    for v in W:
        out.append([(a*2*L)-L for a in v])
    return out