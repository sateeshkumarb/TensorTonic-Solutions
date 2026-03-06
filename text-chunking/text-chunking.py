def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    if not tokens:
        return []
        
    start = 0
    tl = len(tokens)
    output = []

    while True:
        end = start + chunk_size
        if end>=tl:
            ch = tokens[start:]
            output.append(ch)
            break
        else:
            output.append(tokens[start:end])
        start = end - overlap

    return output
    
    