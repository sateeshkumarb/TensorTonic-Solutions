def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    words = {}
    for t in tokens:
        words[t] = True
        
    for s in stopwords:
        words.pop(s,None)
    return list(words.keys())
