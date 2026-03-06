def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    enc = {}
    tot = len(values)
    for v in values:
        if v not in enc:
            enc[v] = 1
        else:
            enc[v] += 1

    out = []
    for v in values:
        out.append(enc[v]/tot)
    return out