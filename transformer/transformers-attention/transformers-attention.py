import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    dk = Q.shape[2]
    qk = torch.matmul(Q, K.transpose(-2, -1))/math.sqrt(dk)
    scores = F.softmax(qk,dim=-1)
    val = torch.matmul(scores,V)
    return val    