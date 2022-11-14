import numpy as np

# pytorch
import torch
from torch import nn
import torch.nn.functional as F


class FeedForwardNN(nn.Module):
    ''' General Feed Forward Neural Network for use by any agent '''
    # TODO: make thius configurable with a config file
    def __init__(self, in_dim, out_dim):
        super(FeedForwardNN, self).__init__()
        # TODO: make this configurable with a config file
        self.layer1 = nn.Linear(in_dim, 64)
        self.layer2 = nn.Linear(64, 64)
        self.layer3 = nn.Linear(64, out_dim)

    def forward(self, obs):
        # Convert observation to tensor if it's a numpy array
        if isinstance(obs, np.ndarray):
            obs = torch.tensor(obs, dtype=torch.float)

        # TODO: make this configurable with a config file
        activation1 = F.relu(self.layer1(obs))
        activation2 = F.relu(self.layer2(activation1))
        output = self.layer3(activation2)
        return output
