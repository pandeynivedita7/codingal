import torch

def fedavg(weight_list):
    avg_weights = {}

    for k in weight_list[0].keys():
        # Average only floating-point tensors
        if weight_list[0][k].dtype in (torch.float16, torch.float32, torch.float64):
            avg_weights[k] = torch.stack(
                [w[k] for w in weight_list], dim=0
            ).mean(dim=0)
        else:
            # Keep integer / non-trainable tensors unchanged
            avg_weights[k] = weight_list[0][k]

    return avg_weights
