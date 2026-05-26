import torch

# 1. 检查 PyTorch 的具体版本号
print(f"PyTorch Version: {torch.__version__}")

# 2. 检查你的 Mac GPU (MPS) 是否可用
# 如果返回 True，说明你的 PyTorch 可以调用 M3 Pro 的 GPU 算力
print(f"MPS (Mac GPU) Available: {torch.backends.mps.is_available()}")

# 3. 检查当前的 PyTorch 编译时是否包含了 MPS 支持
print(f"MPS Built: {torch.backends.mps.is_built()}")

# 4. 作为对比，检查 CUDA (NVIDIA GPU) 是否可用
# 在你的 Mac 上，这个应该返回 False
print(f"CUDA (NVIDIA GPU) Available: {torch.cuda.is_available()}")


# ==== Output ====
# PyTorch Version: 2.12.0
# MPS (Mac GPU) Available: True
# MPS Built: True
# CUDA (NVIDIA GPU) Available: False