---
layout: post
title: "Strong passwords"
---

Life is full of deep philosophical problems that have plagued mankind's best minds for ages:

* What is the meaning of life?
* Why is there something rather than nothing?
* What does it mean to be human?
* How do I choose a strong password?
* How do I get laid without too much effort?

All of these questions remain the subject of much contention even to the present day, especially on the internet where many experts engage in highly nuanced and informative debate. 
Today, however, I will focus on one question in particular:

>How do I choose a strong password?

It is my intention to attempt to analyze this problem here with some mathematical rigor. First of all, we must define what we mean by a "strong password". It should be clear that this 
is an inherently subjective notion that depends on the strength of your expected adversary. As computers become faster and faster, passwords that were once considered "strong" become 
unacceptably weak. Hence, the theory will have to account for this. I will rephrase the question in more exact mathematical terms:

>Given a character set $A$ and an adversary who can brute-force passwords from this set at a speed of $v$ passwords per second. What properties does my password need to satisfy such 
that the adversary needs to spend at least $t$ seconds on average before my password is cracked?

So, we have some alphabet $A$ (eg all characters on the keyboard) and our password must be some string composed of characters from this set alone. Then, there is an adversary who can 
take a hash of our password (perhaps stolen from some online database or whatever) and brute-force it at a rate of $v$ strings per second. The question arises what properties are 
necessary and sufficient for a password to require at least $t$ seconds on average before the adversary can crack it.

Suppose our password was sampled uniformly at random from the set of all strings over $A$ of length $m$. This uniform random sampling guarantees that an adversary can exploit 
no other information they might know about us, such as birthdays or mother's maiden names. The question then becomes how large $m$ must be for an attacker to need an expected time of 
at least $t$ seconds in order to crack the password. There are exactly $|A|^m$ strings of length $m$ over $A$. If we let $Q$ be the number of passwords the attacker needs to 
check, then we find
\begin{equation}
	E[Q] = \sum_{i=1}^{|A|^m} \frac{1}{|A|^m}i = \frac{|A|^m + 1}{2}.
\end{equation}
At a rate of $v$ passwords per second, the number of seconds the attacker will require can be written as
\begin{equation}
	T = \frac{Q}{v}.
\end{equation}
Taking expectations, we find
\begin{equation}
	E[T] = \frac{|A|^m + 1}{2v}.
\end{equation}
We want this value to be at least $\varepsilon$:
\begin{equation}
	\frac{|A|^m + 1}{2v} \geq \varepsilon.
\end{equation}
We can solve the above equation in terms of $m$ or $|A|$ depending on which question we want to answer. If the alphabet $A$ is fixed and the only question is how long our passwords 
must be, then this yields
\begin{equation}
	m \geq \log_{|A|}(2v\varepsilon - 1).
\end{equation}
If the length of the password is fixed and we want to change the alphabet size, then we find
\begin{equation}
	|A| \geq (2v\varepsilon - 1)^{\frac{1}{m}}.
\end{equation}
Note the following nice properties:

1. The size of the password grows logarithmically in the speed of the attacker and the minimal amount of time we want. To show how awesome this is, let's suppose we have a binary 
alphabet $A = \{0,1\}$ and an attacker who can crack a billion passwords per second, ie $v = 10^9$. If we want the attacker to require at least one year on average to crack our 
password, then $\varepsilon = 31,556,926$ and we find $m \geq 56$ (rounded up). Now suppose our attacker doubles their speed, so $v = 2 \times 10^9$. Then, all else being equal, we 
find $m \geq 57$ (rounded up). Doubling their speed only required us to add a single character to our passwords!
2. The size of the alphabet grows linearly in the speed of the attacker and minimal amount of time. It is inversely proportional to the length of the password. Again, to demonstrate, 
suppose we have an attacker that can crack a billion passwords per second, passwords have length 8 and $\varepsilon$ equals one year. Then $|A| \geq 126$. If the attacker doubles 
their speed, we get $|A| \geq 138$, which is an additional 12 characters in the alphabet.

Things don't look as grim as many people might imagine! Indeed, suppose our alphabet consists of commonly used English words. A conservative estimate might put this number somewhere 
around 600. Suppose also that we want an attacker to need at least ten years on average to crack our passwords, and that our adversary might have access to supercomputers. This could 
put their performance somewhere around 350 billion passwords per second. How many words does our password need? Plugging in the numbers and rounding up, we find 8. Eight random 
English words suffice to make an adversary who can process 350 billion passwords per second take on average ten years to succeed! The moral of this story is clear:

>Stop using short, hard-to-remember gibberish as your passwords. Use phrases of at least eight random words. These will be much easier to remember and much more secure.

Of course, there is also a [relevant xkcd](https://xkcd.com/936/).
