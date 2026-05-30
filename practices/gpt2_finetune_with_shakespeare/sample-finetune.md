
### sample on finetune gpt2-medium + shakespeare
```
-> % python sample.py --out_dir=out-shakespeare --device=mps --num_samples=5 --max_new_tokens=100 \
--start="What is the answer to life, the universe, and everything?"
Overriding: out_dir = out-shakespeare
Overriding: device = mps
Overriding: num_samples = 5
Overriding: max_new_tokens = 100
Overriding: start = What is the answer to life, the universe, and everything?
number of parameters: 353.77M
No meta.pkl found, assuming GPT-2 encodings...
====>>>====: start:  What is the answer to life, the universe, and everything?
====>>>====: start_ids:  [2061, 318, 262, 3280, 284, 1204, 11, 262, 6881, 11, 290, 2279, 30]
====>>>====: x:  tensor([[2061,  318,  262, 3280,  284, 1204,   11,  262, 6881,   11,  290, 2279,
           30]], device='mps:0')
====>>>====: Start the generation!!! ====
What is the answer to life, the universe, and everything?

A:
Gentlemen,
The great problem, from the point of view of the human mind, is this, that we are endowed with a state of existence which is not that of a being, but, whether we like it or not, a being which cannot lie down to sleep, and therefore must needs sleep, for the purpose of being alive.

D:
What is the conclusion you draw from this?

A:
I prove it to be true
----- Sample <0> Finished! ----------
What is the answer to life, the universe, and everything?

The answer to life and the universe is to be found in love and joy.

Then love is indeed the answer to all that is simple and to know how happiness, the state of the soul, happiness, happiness, happiness, happiness,
was, and is.

Then the world shall be saved:
Love, the world's salvation, is the answer to every question.

Then love, the world's salvation, is the answer to every question.


----- Sample <1> Finished! ----------
What is the answer to life, the universe, and everything? If you have to answer, know that every thought that comes to your head is a thought,
Your mind is as precious as your body,
Just as you have lost your soul, your heart is as empty,
As you have lost your strength, your strength you lack;
And you must know that you are worth nothing in your whole existence.

But what must I do, if I have not a soul? I must spend my life in this fearful death;
And this
----- Sample <2> Finished! ----------
What is the answer to life, the universe, and everything?
We don't know.
And why not
If you would be most careful?
Let me hear your answers, and try to understand
The mind which is in you, and you, where the mind is
Against it.

VIII

HE:

You are

I say
I am good, I am mad, my soul is dead,
and cannot live in you by your will but you will
Do rather as I do, than as I
----- Sample <3> Finished! ----------
What is the answer to life, the universe, and everything?

Pepys:
Pepys:
All this is your part
To do, O good man,
What has held you in bondage.

Little Jack:
By no means.

Little John:
Do you think a man can be happy?

Little Jack:
I am sure not. I know I am
A creature bound to the ground,
The lowest member of the human race,
A piece of filthy flax,
And
----- Sample <4> Finished! ----------
```

### sample on gpt2-medium
```
joy@joys-MacBook-Pro [19:27:41] [~/Git/nanogpt] [master *]
-> % python sample.py --init_from=gpt2-medium --device=mps --num_samples=5 --max_new_tokens=100 \
--start="What is the answer to life, the universe, and everything?"
Overriding: init_from = gpt2-medium
Overriding: device = mps
Overriding: num_samples = 5
Overriding: max_new_tokens = 100
Overriding: start = What is the answer to life, the universe, and everything?
loading weights from pretrained gpt: gpt2-medium
forcing vocab_size=50257, block_size=1024, bias=True
overriding dropout rate to 0.0
number of parameters: 353.77M
Loading weights: 100%|█████████████████████████████████████████████████████████████████████████| 292/292 [00:00<00:00, 65754.15it/s]
No meta.pkl found, assuming GPT-2 encodings...
====>>>====: start:  What is the answer to life, the universe, and everything?
====>>>====: start_ids:  [2061, 318, 262, 3280, 284, 1204, 11, 262, 6881, 11, 290, 2279, 30]
====>>>====: x:  tensor([[2061,  318,  262, 3280,  284, 1204,   11,  262, 6881,   11,  290, 2279,
           30]], device='mps:0')
====>>>====: Start the generation!!! ====
What is the answer to life, the universe, and everything?

Here is what you need to know.

1. The life we live is the most important thing in the universe, but we are only living it because it is right.

2. I am the universe but I am not a part of it. I cannot change who I am or what I will become.

3. Everything changed when God created the universe. The same people who created you are the ones who should be destroyed.

4. There will be
----- Sample <0> Finished! ----------
What is the answer to life, the universe, and everything? Should I help or hinder? What am I or am I not?

However, the answer to these questions is not straightforward, as that answer depends on how we understand happiness, meaning, and the existence of happiness itself.

In the philosophical world, although the standard of existence and happiness depends on the existence of the soul, the existence of the soul is not the standard of existence or happiness. In fact, both the soul and happiness are subjective. In order to measure the subjective experience
----- Sample <1> Finished! ----------
What is the answer to life, the universe, and everything? These two questions are the key to understanding the existence of God, and the reason that Jesus was chosen by the Father and knows everything.

What is the evidence of the Trinity?

This is one of the most difficult questions to answer. The Bible doesn't tell us how the Trinity is made, but it does say that God created the Father, Son, and Holy Spirit in three parts. The Father and Son were created from nothing and were not formed in a manner similar to the average
----- Sample <2> Finished! ----------
What is the answer to life, the universe, and everything?


A man must be wise to know how

the Universe draws its power from the

first man; for he must know the

previous, how the first man came into

the universe." In other words, how can we

know how will the Universe draw

its power from the first man?


The second rule: he must be wise to know how

the Universe draws its power from

the first man, for he must know
----- Sample <3> Finished! ----------
What is the answer to life, the universe, and everything? How do we get there? Why do we exist? As you read this, you can have a vivid, vivid experience, a profound experience. You can have an infinite experience, which will bring you to a depth of understanding."

They weren't satisfied with the Earth-Moon system. They wanted to understand beyond the physical. So they started thinking about what's beyond the spacetime system, what's beyond our solar system. And what they realized was that what was beyond the solar system was
----- Sample <4> Finished! ----------
```