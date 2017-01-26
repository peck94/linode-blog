---
title: "The Most Efficient Copypasta"
date: 2017-01-19
layout: post
---
An interesting question I read on the internet a while ago is the following:

>Suppose you have an editor that allows you to select, copy and paste any amount of text already written in it.
Now suppose you want to use that editor to type out some known body of text. What would be the most efficient way to do so?

This is basically a question about *compression*. Given some alphabet $$\Sigma$$ and the following operations:

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
by a shorter copypasta than the one the above algorithm would construct. The key insight is that sometimes, it is more efficient to paste a substring of the text somewhere
other than the end of the buffer; sometimes we may have to copy a part of the string and paste it right in the middle somewhere. This is something our algorithm will never do,
and as such it cannot be optimal. For example, suppose we want an optimal copypasta for the following string:

    aaaabbbb

Since this string is so short, our algorithm will output a worst-case copypasta, ie of length 8. There is, however, a more efficient approach:

    Print(a)
    Print(a)
    Print(b)
    Print(b)
    Copy(1,4)
    Paste(2)

This copypasta has length 6, which is clearly superior. What's worse, this pattern may be extended as follows. Suppose $$s = a^kb^k$$, ie the symbol `a` repeated $$k$$ times followed by the symbol `b`
repeated $$k$$ times. Suppose also for simplicity that $$k$$ is a power of two, say $$k = 2^n$$ where $$n \geq 2$$. Then our algorithm will construct the following copypasta:

    Print(a)
    Print(a)
    Print(a)
    Print(a)
    Copy(1,4)
    Paste(4)
    Copy(1,8)
    Paste(8)
    ...
    Copy(1, 2**(k-1))
    Paste(2**(k-1))
    Print(b)
    Print(b)
    Print(b)
    Print(b)
    Copy(2**k+1,2**k+4)
    Paste(2**k+4)
    Copy(2**k+1,2**k+8)
    Paste(2**k+8)
    ...
    Copy(2**k+1, 2**k+2**(k-1))
    Paste(2**k+2**(k-1))

This copypasta has length $$4n$$. However, a better copypasta simply does this:

    Print(a)
    Print(a)
    Print(b)
    Print(b)
    Copy(1,4)
    Paste(2)
    Copy(1,8)
    Paste(4)
    ...
    Copy(1,2**k)
    Paste(2**(k-1))

This copypasta has length $$2n$$, meaning it will always be half as long as what our algorithm puts out. So in the worst case, our algorithm can produce a copypasta that is still at least
twice as long as the shortest possible one! Although the nature of the counter-example is very illuminating, it brings us to a rather depressing conclusion: in order to find the smallest
copypasta for a given string, we would have to do some serious analysis to find out how the structure of the string may be optimally exploited. How this can be done efficiently is not quite clear.

It is possible to go completely meta with this. For example, we can construct copypastas that output other copypastas. To do this, suppose we have a copypasta $$P$$ for a string $$s$$ over an
alphabet $$\Sigma$$. We can then construct a new alphabet $$\Sigma^\prime$$ as follows:

$$\begin{aligned}
    \Sigma^\prime = \{ \mathrm{Print}(a) \mid a \in \Sigma \} \cup \{ \mathrm{Copy}(i,j) \mid 0 < i \leq j \leq |s| \} \cup \{ \mathrm{Paste}(i) \mid 0 < i \leq |s| \}.
\end{aligned}$$

The resulting alphabet is clearly still finite. Moreover, $$\Sigma^\prime$$ has the property that every copypasta for a string over $$\Sigma$$ is itself a string over $$\Sigma^\prime$$.
Hence, using $$\Sigma^\prime$$, we can construct copypastas that output copypastas for strings over $$\Sigma$$. There is no end to how deep one can go with this: repeating the same procedure
as much as we want, we can obtain copypastas that construct copypastas that construct copypastas ... that construct copypastas for strings over $$\Sigma$$.

Now suppose we have an algorithm $$A$$ written in some programming language $$L$$ that, on input a string $$s$$ over $$\Sigma$$, outputs the optimal copypasta $$s^\star$$.
Note that, since $$A$$ is written in $$L$$, the code of $$A$$ is itself a string over the alphabet of $$L$$.
We can supply $$A$$ with its own source code as input and, by definition, it should output an optimal copypasta $$A^\star$$ for itself.