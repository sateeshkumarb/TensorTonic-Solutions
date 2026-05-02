import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    out = []
    x = torch.tensor(x)
    if method=="relu":
        out = torch.where(x>0,x,0.0)
    elif method == 'leaky_relu':
        out = torch.where(x>0,x,0.01*x)
    elif method== "sigmoid":
        out = 1/(1+torch.exp(-x))
    elif method == "tanh":
        nr = torch.exp(x) - torch.exp(-x)
        dr = torch.exp(x) + torch.exp(-x)
        out = nr/dr
    return out
    
                
    