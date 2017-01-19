---
title: "The Most Efficient Copypasta"
date: 2017-01-19
layout: post
---
An interesting question I read on the internet a while ago is the following:

>Suppose you have an editor that allows you to select, copy and paste any amount of text already written in it.
Now suppose you want to use that editor to type out some known body of text. What would be the most efficient way to do so?

This is basically a question about *compression*. Given some alphabet $\Sigma$ and the following operations:

* `Print(a)`: print the symbol `a` to the output;

* `Copy(i,j)`: select all characters from the $$i$$th to the $$j$$th inclusive and copy them to the clipboard;

* `Paste(i)`: insert the contents of the clipboard right after the $$i$$th character.

I define a *copypasta* to be any sequence of these operations satisfying the following properties:

1. each call to `Print(a)` has $$a \in \Sigma$$;

2. each call to `Copy(i,j)` has $$0 < i \leq j < n$$ where $$n$$ is the length of the output buffer;

3. each call to `Paste(i)` has $$0 < i \leq n$$ where $$n$$ is the length of the output buffer.

Thus, a copypasta can be seen as a "program" for typing out some specific string. The *length* $$|P|$$ of a copypasta $$P$$ can be defined as the number of operations it contains.
The question is now:

>Given a string $$s$$ over alphabet $$\Sigma$$. What is the smallest copypasta that outputs $$s$$?

We denote the smallest copypasta for a string $$s$$ as $$s^\star$$. Clearly
\begin{equation}
    |s^\star| \leq |s|
\end{equation}
since the most basic copypasta for a string $$s = s_1 \dots s_k$$ is the following:

    Print(s[1])
    ...
    Print(s[k])

How could we possibly design shorter copypastas? The trick is to exploit *redundancies* within the string $$s$$.
For example, suppose $$s$$ is just the symbol `a` repeated 256 times. An efficient copypasta would then perform the following operations:

    Print(a)
    Print(a)
    Print(a)
    Print(a)
    Copy(1,4)
    Paste(4)
    Copy(1,8)
    Paste(8)
    Copy(1,16)
    Paste(16)
    Copy(1,32)
    Paste(32)
    Copy(1,64)
    Paste(64)
    Copy(1,128)
    Paste(128)

Instead of the maximum of 256 print operations, we accomplished this using only 16, which is about 94% shorter.
A general strategy could be the following. Suppose we already printed out $$k$$ characters of the string $$s$$.
We could then search for the longest substring in the output buffer that also appears at the start of the rest of $$s$$ that we still need to print.
If this substring is longer than two characters, it is more efficient to copy and paste it than it is to type it out.
If no such substring exists, we simply type out the actual next character of $$s$$ directly. Repeating this strategy until $$s$$ is fully printed
yields an algorithm that is already significantly better than worst-case. If this sounds familiar, it's because this idea is actually used in some
practical compression algorithms, such as [LZ77](https://en.wikipedia.org/wiki/LZ77_and_LZ78).

Two questions remain:

1. Is the output of this algorithm optimal? That is, does it actually output the smallest copypasta?

2. What is the algorithm's runtime?

The second question is actually very easy to answer: assuming we do a brute force search for the longest substring (which is bad, since much more efficient algorithms
exist for these purposes), we find we have to perform at most $$i$$ operations in iteration $$i$$ of the algorithm. This means a worst-case runtime of $$O(|s|^2)$$.
This runtime can definitely be improved upon by using faster string searching algorithms, but the point is that it's most certainly polynomial-time.

A much more interesting question is if this algorithm is optimal. The easiest way to prove it's not would be to provide a counter-example: a string that can be produced
by a shorter copypasta than the one the above algorithm would construct.