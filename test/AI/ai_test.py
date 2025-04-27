#!/usr/bin/env python3

import torch

print(torch.coda.is_available())
print(torch.version.cuda)
print(torch.backends.cudnn.version())