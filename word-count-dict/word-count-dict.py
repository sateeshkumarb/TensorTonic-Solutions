def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    out = {}
    for s in sentences:
        for w in s:
            if w not in out:
                out[w] = 0
            out[w] += 1
    return out