import torch
import torch.nn as nn
import torch.optim as optim

#Initialze the device
device= {
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
}

print(f"Using device: {device}")

device =device.pop()

class Word2Vec(nn.Module):
    def __init__(self,n,m):
    