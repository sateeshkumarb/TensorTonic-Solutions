import math

def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    cos_term = 1.0  + math.cos(math.pi*current_step/total_steps)
    lr = min_lr + 0.5 * (base_lr - min_lr) * cos_term
    return lr