import torch

# 1. 把快照加载到系统内存 (CPU)
checkpoint = torch.load('out-shakespeare-char/ckpt.pt', map_location='cpu')

# 2. 提取出模型的状态字典
state_dict = checkpoint['model']

# 3. 打印它到底长什么样
for key, tensor in state_dict.items():
    # 我们只打印每一层的名字和它张量的形状 (Shape)，防止巨量的浮点数刷屏
    print(f"Layer Name: {key: <45} | Shape: {tensor.shape}")