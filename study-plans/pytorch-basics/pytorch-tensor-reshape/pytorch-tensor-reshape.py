import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    
    x = torch.tensor(x,dtype=torch.float32)
    
    if op == "flatten":
        x = torch.flatten(x)
    elif op == "squeeze":
        x = torch.squeeze(x)
    elif op == "transpose":
        x = x.permute(1,0)
    else:
        pass
    return x.tolist()
    
