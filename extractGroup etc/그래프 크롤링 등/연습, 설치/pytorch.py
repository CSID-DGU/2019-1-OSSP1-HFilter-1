import numpy as np
import torch

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)

x = torch.rand(5, 3)
print(x)

x = torch.zeros(5, 4, dtype=torch.long)
print(x)
print(x.size())
print(x[:, 1])
print(x[:, 1:2])

x= torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8) # -1이면 다른 차원이용해 유추
print(x.size(), y.size(), z.size())
print(x)
print(y)
print(z)

a = torch.ones(5)
b = a.numpy()
a.add_(1)
print(a)
print(b)

c = np.ones(6)
d = torch.from_numpy(c)
np.add(c, 1, out=c)
print(c)
print(d)
