
## Finetune on gpt2-medium
```
$ python data/shakespeare/prepare.py
train has 301,966 tokens
val has 36,059 tokens

$ python train.py config/finetune_shakespeare.py --init_from=gpt2-medium --device=mps \
    --compile=False \
    --eval_interval=10 \
    --eval_iters=5 \
    --log_interval=1
Overriding config with config/finetune_shakespeare.py:
import time

out_dir = 'out-shakespeare'
eval_interval = 5
eval_iters = 40
wandb_log = False # feel free to turn on
wandb_project = 'shakespeare'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'shakespeare'
init_from = 'gpt2-xl' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 20

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False

Overriding: init_from = gpt2-medium
Overriding: device = mps
Overriding: compile = False
Overriding: eval_interval = 10
Overriding: eval_iters = 5
Overriding: log_interval = 1
tokens per iteration will be: 32,768
Initializing from OpenAI GPT-2 weights: gpt2-medium
loading weights from pretrained gpt: gpt2-medium
forcing vocab_size=50257, block_size=1024, bias=True
overriding dropout rate to 0.0
number of parameters: 353.77M
config.json: 100%|█████████████████████████████████████████████████████████████████████████████████| 718/718 [00:00<00:00, 1.02MB/s]
model.safetensors: 100%|███████████████████████████████████████████████████████████████████████| 1.52G/1.52G [01:33<00:00, 16.2MB/s]
Loading weights: 100%|█████████████████████████████████████████████████████████████████████████| 292/292 [00:00<00:00, 61628.18it/s]
generation_config.json: 100%|███████████████████████████████████████████████████████████████████████| 124/124 [00:00<00:00, 138kB/s]
/Users/joy/Git/nanogpt/train.py:196: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  scaler = torch.cuda.amp.GradScaler(enabled=(dtype == 'float16'))
/Users/joy/Git/nanogpt/.venv/lib/python3.10/site-packages/torch/cuda/amp/grad_scaler.py:31: UserWarning: torch.cuda.amp.GradScaler is enabled, but CUDA is not available.  Disabling.
  super().__init__(
num decayed parameter tensors: 98, with 354,501,632 parameters
num non-decayed parameter tensors: 194, with 321,536 parameters
using fused AdamW: False
step 0: train loss 3.7666, val loss 3.6606
iter 0: loss 3.2649, time 32146.62ms, mfu -100.00%
iter 1: loss 3.4618, time 28420.70ms, mfu -100.00%
iter 2: loss 3.4011, time 28508.58ms, mfu -100.00%
iter 3: loss 3.8040, time 28355.38ms, mfu -100.00%
iter 4: loss 2.5250, time 28523.34ms, mfu -100.00%
iter 5: loss 3.5501, time 28710.24ms, mfu 0.89%
iter 6: loss 3.8274, time 28914.18ms, mfu 0.89%
iter 7: loss 3.8138, time 28660.73ms, mfu 0.89%
iter 8: loss 3.3780, time 28556.49ms, mfu 0.89%
iter 9: loss 3.6405, time 30321.46ms, mfu 0.88%
step 10: train loss 3.1114, val loss 3.0547
saving checkpoint to out-shakespeare
iter 10: loss 2.8899, time 36432.42ms, mfu 0.86%
iter 11: loss 3.5762, time 28308.15ms, mfu 0.87%
iter 12: loss 3.2994, time 28323.45ms, mfu 0.87%
iter 13: loss 3.1303, time 28326.16ms, mfu 0.87%
iter 14: loss 3.4361, time 29691.86ms, mfu 0.87%
iter 15: loss 3.3191, time 29551.22ms, mfu 0.87%
iter 16: loss 3.0338, time 28661.96ms, mfu 0.87%
iter 17: loss 3.2062, time 28677.88ms, mfu 0.87%
iter 18: loss 3.3461, time 28272.74ms, mfu 0.88%
iter 19: loss 3.2203, time 28285.45ms, mfu 0.88%
step 20: train loss 3.3216, val loss 2.8432
saving checkpoint to out-shakespeare
iter 20: loss 3.5170, time 34725.19ms, mfu 0.86%
```