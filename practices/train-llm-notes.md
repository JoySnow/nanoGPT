



## Basic Concepts

### Dropout (随机失活)

`dropout = 0.0 # for pretraining 0 is good, for finetuning try 0.1+`

屏蔽/停用 10% 的参数 -> 强迫这一轮训练不依赖这些节点 -> 最终让整个模型不依赖单一/相似的路径


### decay_lr - Learning Rate Decay (学习率衰减)

`decay_lr = True # whether to decay the learning rate`

含义：随着训练步数的增加，系统自动把“步长（Learning Rate）”逐渐调小。

这是优化器（Optimizer）层面的全局调度策略。

### Weight Decay (权重衰减)

另一个极易混淆的概念  - 这是针对模型千万个参数的“财富剥夺”策略，用来防止过拟合。
它的含义：在每次更新参数时，系统会强行把所有权重参数自身的值乘以一个小于 1 的数字（比如 $0.99$），让它们在数值上产生一点点“缩水”。它不会把任何参数屏蔽成 0，它只是让大家集体变小。

为什么需要它？ 神经网络很容易产生“惰性”，如果某个特征（比如单词 "the"）经常出现，对应的神经元权重就会变得极其巨大，最终模型变成了一个只会根据单一特征做决定的“偏科生”。

### Model = Pre-training + SFT + RLHF

the Pre-training takes 99% on Data and calculation, the data goes wild.
the SFT and RLHF takes 1% , but the Data is extra "expensive".

#### 指令微调 (SFT - Supervised Fine-Tuning)
用结构话数据做：
```
{
    "instruction": "你是一个资深的 DBA。请根据用户的需求输出 PostgreSQL 语句。不要解释，只输出代码。",
    "input": "查询 users 表里昨天注册的活跃用户。",
    "output": "SELECT * FROM users WHERE status = 'active' AND created_at >= CURRENT_DATE - INTERVAL '1 day';"
},
```

#### 人类反馈强化学习 (RLHF - Reinforcement Learning from Human Feedback)

eg. OpenAI 会让 SFT 后的模型对同一个问题生成 4 个不同的答案。
然后让人类标注员对这 4 个答案进行“点赞/踩”的排序。
系统用这些排序数据训练出一个“裁判模型”。
最后，主模型在不断自我生成的过程中，裁判模型会实时给它打分，通过强化学习（PPO 算法）逼迫主模型越来越符合人类的胃口。


## my notes

### Q: for the finetune result, with only max_iters = 20 round fine-tune, the output already 完全是莎士比亚对话的味道了. how this ?
say.
    """What is the answer to life, the universe, and everything?

    Pepys:
    Pepys:
    All this is your part
    To do, O good man,
    What has held you in bondage.

    Little Jack:
    By no means.
    """
Answer：
    这是理解迁移学习 (Transfer Learning) 最重要的一点。
    base model 里早就存在一个极其庞大、完美的“莎士比亚知识区”。
    这20 步微调，只是在修改系统的默认路由规则 (Default Routing Rule)。你通过梯度的轻微推拉，给所有指向“现代英语”的路由加了**惩罚权重**，给所有指向“莎士比亚区”的**路由加了极大的提权**。模型其实只是被你“唤醒”了特定的记忆。
