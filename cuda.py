import torch
print("Is cuDNN enabled: ", torch.backends.cudnn.enabled)
print("cuDNN version: ", torch.backends.cudnn.version())
