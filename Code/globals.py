import torch
import torch.backends.mps


DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
NUM_CLASSES = 7
BATCH_SIZE = 256
LR = 1e-3               # The initial Learning Rate
MOMENTUM = 0.9          # Hyperparameter for SGD, keep this at 0.9 when using SGD
WEIGHT_DECAY = 5e-5     # Regularization, you can keep this at the default
NUM_EPOCHS = 30         # Total number of training epochs (iterations over dataset)
STEP_SIZE = 20          # How many epochs before decreasing learning rate (if using a step-down policy)
GAMMA = 0.1             # Multiplicative factor for learning rate step-down

LOG_FREQUENCY = 10


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

CONFIG = dotdict({})

if torch.cuda.is_available():
    CONFIG.device = 'cuda'
elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
    CONFIG.device = 'mps'
else:
    CONFIG.device = 'cpu'

CONFIG.dtype = torch.float32
