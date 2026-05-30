### on the local trained gpt2 with max_iters=50 :D

Cute!!! 爱编点 the \n ,. and of

#### Case-A
```
$ python sample.py --out_dir=out --device=mps --num_samples=5 --max_new_tokens=10 --start="hello"
Overriding: out_dir = out
Overriding: device = mps
Overriding: num_samples = 5
Overriding: max_new_tokens = 10
Overriding: start = hello
number of parameters: 123.59M
No meta.pkl found, assuming GPT-2 encodings...
====>>>====: start:  hello
====>>>====: start_ids:  [31373]
====>>>====: x:  tensor([[31373]], device='mps:0')
====>>>====: Start the generation!!! ====
hello,,,,,,.



----- Sample <0> Finished! ----------
hello,,,,,ampa, to,,
----- Sample <1> Finished! ----------
hello of the to the much worthless, the of the
----- Sample <2> Finished! ----------
hello.









----- Sample <3> Finished! ----------
hello, and.







----- Sample <4> Finished! ----------
```

#### Case-B
```
$ python sample.py --out_dir=out --device=mps --num_samples=5 --max_new_tokens=10 \
--start="What is the answer to life, the universe, and everything?"
Overriding: out_dir = out
Overriding: device = mps
Overriding: num_samples = 5
Overriding: max_new_tokens = 10
Overriding: start = What is the answer to life, the universe, and everything?
number of parameters: 123.59M
No meta.pkl found, assuming GPT-2 encodings...
====>>>====: start:  What is the answer to life, the universe, and everything?
====>>>====: start_ids:  [2061, 318, 262, 3280, 284, 1204, 11, 262, 6881, 11, 290, 2279, 30]
====>>>====: x:  tensor([[2061,  318,  262, 3280,  284, 1204,   11,  262, 6881,   11,  290, 2279,
           30]], device='mps:0')
====>>>====: Start the generation!!! ====
What is the answer to life, the universe, and everything? and the.







----- Sample <0> Finished! ----------
What is the answer to life, the universe, and everything?,, the.






----- Sample <1> Finished! ----------
What is the answer to life, the universe, and everything? of the to the.





----- Sample <2> Finished! ----------
What is the answer to life, the universe, and everything?.
```








----- Sample <3> Finished! ----------
What is the answer to life, the universe, and everything?, the.







----- Sample <4> Finished! ----------
