# import torch
# M = torch.tensor([[0.2,0.6,1,0.2],[4/15,0,0,0.4],[4/15,0,0,0.4],[4/15,0.4,0,0]])
# v = torch.tensor([0.25,0.25,0.25,0.25])
# iter = 2
# for i in range(iter):
#     res = torch.mv(M,v)
#     print(res)

import torch
M = torch.tensor([[0.1,0.5,0.9,0.1],[4/15,0,0,0.4],[4/15+0.1,0.1,0.1,0.5],[4/15,0.4,0,0]])
v = torch.tensor([0.25,0.25,0.25,0.25])
iter = 2
for i in range(iter):
    res = torch.mv(M,v)
    print(res)