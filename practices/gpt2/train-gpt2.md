


### Tokenization with num_proc=8
CPU 密集型任务 - 8 processes, 1 thread each for py; high CPU, low MEM.

~~~
PID    COMMAND      %CPU TIME     #TH    #WQ  #PORT MEM    PURG   CMPRS  PGRP  PPID  STATE    BOOSTS          %CPU_ME %CPU_OTHRS
17494  python3.10   78.6 02:40.52 1/1    0    8     244M+  0B     97M-   16551 16551 running  *0[1]           0.00000 0.00000
17498  python3.10   78.4 02:40.85 1/1    0    8     229M+  0B     19M-   16551 16551 running  *0[1]           0.00000 0.00000
17493  python3.10   78.3 02:40.88 1/1    0    8     231M+  0B     89M    16551 16551 running  *0[1]           0.00000 0.00000
17495  python3.10   78.2 02:40.61 1/1    0    8     226M+  0B     89M-   16551 16551 running  *0[1]           0.00000 0.00000
17497  python3.10   78.1 02:40.60 1/1    0    8     234M+  0B     21M-   16551 16551 running  *0[1]           0.00000 0.00000
17500  python3.10   78.1 02:40.26 1/1    0    8     222M-  0B     19M    16551 16551 running  *0[1]           0.00000 0.00000
17499  python3.10   77.8 02:40.60 1      0    8     237M+  0B     18M-   16551 16551 sleeping *0[1]           0.00000 0.00000
17496  python3.10   76.9 02:39.99 1/1    0    8     228M+  0B     17M-   16551 16551 running  *0[1]           0.00000 0.00000
~~~

### Training on mps

Mac M3 Pro 正在以极其标准的姿态执行 AI 训练任务：大显存驻留(high MEM) + CPU 轻量调度 + 极高强度的底层协处理器 (GPU) 阻塞等待。

~~~
PID    COMMAND      %CPU TIME     #TH    #WQ  #PORT MEM    PURG   CMPRS  PGRP  PPID  STATE    BOOSTS          %CPU_ME %CPU_OTHRS
12988  Google Chrom 30.3 29:19.87 22     1    239   708M+  16K    50M    3967  3967  sleeping *0[759903+]     0.00000 0.00000
22572  python3.10   7.3  00:29.97 7      4    95    6407M+ 3984K  0B     22572 11730 stuck    *0[1]           0.00000 0.00000
0      kernel_task  6.6  20:17.32 660/12 0    0     9104K  0B     0B     0     0     running   0[0]           0.00000 0.00000
23286  top          6.2  00:04.16 1/1    0    28    8768K  0B     0B     23286 17179 running  *0[1]           0.00000 0.00000
~~~