---
title: "A Faster Algorithm or a Faster Computer?"
date: 2017-01-18
layout: post
---

As a dedicated computer nerd, there are but few rare occasions when I venture outside of my little man cave and interact with the world through means that do not involve transistors. 
But when I do, and when people inevitably find out what my occupation is since I am incapable of talking about anything else whatsoever, a question that frequently arises is the 
following:

>Why do we need faster algorithms? Aren't computers getting faster all the time? Why not simply run the algorithm on a faster computer?

Questions like these always make me feel fuzzy and warm inside, because they give me an excuse to continue ranting about things that only interest me with no regard to the interests 
of my interlocutor. But since they asked, I will explain.

Suppose we have an algorithm $$A$$ which takes $$T(n)$$ steps to solve an input of size $$n$$. Suppose also that we have two computers that can process $$v_1$$ and $$\alpha v_1$$ 
instructions per second, respectively. We may ask what the largest instance is that $$A$$ can solve within a certain time bound $$t$$ when run on either computer. Denote these 
quantities by $$N_1$$ and $$N_2$$, respectively, then these are simply the solutions of the following equations:

$$\begin{aligned}
	T(N_1) &= v_1t\\
	T(N_2) &= \alpha v_1t = \alpha T(N_1)
\end{aligned}$$

We can test these equations out on several concrete classes of algorithms to see what they have to say.

1. First, let's check out the famous class **P** of polynomial-time algorithms. If $$A$$ is a polynomial-time algorithm, then $$T(n) = n^d$$ for some $$d > 0$$. We find
\begin{equation}
	N_2 = \alpha^{\frac{1}{d}}N_1.
\end{equation}
For $$d = 1$$ this becomes a perfectly linear relationship between $$N_1$$ and $$N_2$$. However, for larger $$d$$, the effect of a larger $$\alpha$$ diminishes quickly. For example, 
if we want $$N_2 = 2N_1$$ and if $$d=2$$, then $$\alpha = 4$$, meaning our computer needs to become four times as fast to solve twice as many instances using a quadratic algorithm.

2. Now let's take a look at another formidable class of algorithms, those that run in exponential time (the associated complexity class is known as **EXP**). These algorithms satisfy 
$$T(n) = 2^{n^d}$$. For simplicity's sake, let's set $$T(n) = 2^n$$, then we find
\begin{equation}
	N_2 = N_1 + \log_2\alpha.
\end{equation}
So now, if $$\alpha = 2$$, then $$N_2 = N_1 + 1$$. That is, if our computer becomes twice as fast, we can only solve a single larger instance! That is absolutely horrendous.

3. Another important class of algorithms are those that run in log-linear time. Here, $$T(n) = n\log n$$, and
\begin{equation}
	N_2\log N_2 = \alpha N_1\log N_1.
\end{equation}
Let $$N_2 = N_1 + 1$$ for simplicity, then
\begin{equation}
	\alpha = \frac{(N_1 + 1)\log(N_1 + 1)}{N_1 \log N_1} = \frac{N_1+1}{N_1}\frac{\log(N_1+1)}{\log N_1}.
\end{equation}
If $$N_1$$ is large, this can be approximated as
\begin{equation}
	\alpha \approx \frac{N_1+1}{N_1} = 1 + \frac{1}{N_1}.
\end{equation}
Especially for large $$N_1$$, the difference between this and a linear algorithm is negligible.

The lesson to be learned here is simple:

>A faster algorithm almost always beats a faster computer.

"Almost always", in the sense that, if your algorithm is linear or log-linear, the benefits of a faster computer can be very real. However, for many problems such as the NP-hard ones, 
many state-of-the-art algorithms have a worst case execution time that is exponential or at least superpolynomial in the input size. It is simply not enough to have a faster computer 
in these cases; the algorithm is just so incredibly shit that no amount of brilliant hardware is going to keep the stench from getting out. We just need a better algorithm.

This argument applies equally well to memory consumption instead of time, so we can additionally state

>A more memory-efficient algorithm always beats a computer with more memory.

This also means we shouldn't put all our eggs in Moore's basket. Even if Moore's law continues to hold (which is debatable), it won't help us solve realistic instances of NP-hard 
problems anytime soon. We really need faster algorithms; it would take too long to wait for faster computers. According to the above theory and Moore's law, if we currently can solve 
some problem up to input size $$N_1$$ using an $$O(2^n)$$ algorithm, and if we want to solve instances of size $$N_1 + 50$$ without improving our algorithm, then we could easily have 
to wait 100 years for that to be feasible!
