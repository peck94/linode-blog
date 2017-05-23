---
title: The Mathematics of Insurance
date: 2017-05-23
layout: post
---
The basic idea behind insurance is simple.
There are certain threats in this world, such as disease or natural disasters, which happen essentially at random
and which can wreak havoc in people's lives. When such catastrophes occur, it's usually no one's fault,
and so the victims cannot demand compensation from the perpetrators. Indeed, the perpetrators are either forces
of nature, microscopic organisms or other things which cannot actually pay anything back. Moreover, the damages
may be so great that the victims would be financially ruined if they were to pay for repairs themselves.
To overcome this issue, insurance is introduced. Basically, you have a group of people who all might be subject
to some random catastrophe which could cost them a great deal of money, so together they save money into one
account. If anyone ever needs it, the money in the account can be used to pay for whatever damages they incurred.

Formally, let's say we have a set of $$n$$ people and a set of $$m$$ catastrophes. Each catastrophe has a certain
probability of occuring to a given person during a certain time span, let's say one year. However, a person's
particular lifestyle may increase or decrease the probability of a given catastrophe happening to them.
Thus, we introduce a probability matrix $$P$$ where $$p_{ij}$$ is the probability that catastrophe $$i$$ happens
to person $$j$$ in the course of one year. Note that these probabilities need not sum to one; indeed, it's
perfectly possible that no catastrophe happens to person $$j$$ for a whole year.
Each catastrophe also causes a certain amount of damage. To simplify matters, we will assume catastrophe $$i$$
has a single associated cost of repair $$c_i$$ which does not vary by person.

We now want to organise insurance for each of these $$n$$ people, like an insurance company.
The basic question is this:

>How much do we charge each person in yearly premiums so that the company makes a profit?

To find out, we need to quantify the expected amount each person will cost the company in damages this year.
We then need to charge each person a premium which is equal to that cost plus a profit margin.
The expected cost of person $$j$$ is given by

$$
    E[Q_j] = \sum_{i=1}^m p_{ij}c_i.
$$

Hence our total expected cost is

$$
    E[Q] = \sum_{j=1}^n E[Q_j].
$$

If we want to make a profit $$k$$, then we might achieve this by dividing $$k$$ evenly among the $$n$$ insured people.
Person $$j$$'s premium is then given by

$$
    r_j = E[Q_j] + \frac{k}{n}.
$$

Our expected profit is

$$
    E[R] = \sum_{j=1}^n(r_j - E[Q_j]).
$$

In this case, we clearly have $$E[R] = k$$.

As an example, we consider a fictional society with five individuals and three catastrophes they can be insured against:
diabetes, lung cancer and all forms of property damage. The probabilities for each individual are summarized in the table below.

<table style="border-top: solid double; border-bottom: solid double; border-left: 0; border-right: 0">
    <caption>Individual risk for diabetes, lung cancer and property damage</caption>
    <thead>
        <tr>
            <th>Person</th>
            <th>Diabetes</th>
            <th>Lung cancer</th>
            <th>Property damage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>0.1</td>
            <td>0.2</td>
            <td>0.3</td>
        </tr>
        <tr>
            <td>2</td>
            <td>0.7</td>
            <td>0.7</td>
            <td>0.7</td>
        </tr>
        <tr>
            <td>3</td>
            <td>0.7</td>
            <td>0.1</td>
            <td>0.1</td>
        </tr>
        <tr>
            <td>4</td>
            <td>0.1</td>
            <td>0.7</td>
            <td>0.1</td>
        </tr>
        <tr style="border-bottom: solid double">
            <td>5</td>
            <td>0.1</td>
            <td>0.1</td>
            <td>0.7</td>
        </tr>
    </tbody>
</table>

We also summarize the costs of the different afflictions below:

<table style="border-top: solid double; border-bottom: solid double; border-left: 0; border-right: 0">
    <caption>Costs for diabetes, lung cancer and property damage</caption>
    <thead>
        <tr>
            <th>Diabetes</th>
            <th>Lung cancer</th>
            <th>Property damage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>3500</td>
            <td>7000</td>
            <td>1200</td>
        </tr>
    </tbody>
</table>

The expected costs for the different individuals would be as follows:

<table style="border-top: solid double; border-bottom: solid double; border-left: 0; border-right: 0">
    <caption>Annual expected costs for each individual</caption>
    <thead>
        <tr>
            <th>Person</th>
            <th>Expected cost</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>2110</td>
        </tr>
        <tr>
            <td>2</td>
            <td>8190</td>
        </tr>
        <tr>
            <td>3</td>
            <td>3270</td>
        </tr>
        <tr>
            <td>4</td>
            <td>5370</td>
        </tr>
        <tr style="border-bottom: solid double">
            <td>5</td>
            <td>1890</td>
        </tr>
    </tbody>
</table>

Individual 1 has a supremely average life and is not at risk for particularly anything.
Individual 2 has a rather unfortunate life and is at risk for everything he can be insured for.
Individuals 3, 4 and 5 each lead certain lives which put them at heightened risk for specific afflictions.
Now, if our company wants to make a profit of $$k$$, then the annual premium of each individual can be computed
by adding $$k/5$$ to the expected costs.

Note that as the number of people $$n$$ increases, the profit margin decreases towards zero and the insurance premiums
will tend toward the expected cost of each individual. Furthermore, the individual insurance premiums are independent:
one person's bad luck will not raise the premiums of others. Yet, some people may object to this scheme because it does
not charge everyone equally. Indeed, this scheme will obviously charge higher premiums for people at greater risk of
catastrophe. Arguably, these people are often those least able to make such payments.

We may therefore imagine a different insurance scheme than the one described above.
Specifically, what if we were to "pool" the collective risk of each catastrophe and charge people based on that?
Formally, we simply take the total expected cost of all people, $$E[Q]$$, average it and add our profit margin:

$$
    r = \frac{E[Q] + k}{n}.
$$

We then charge each person the same premium $$r$$ instead of the "personalized" premiums $$r_j$$.
In our hypothetical society, we have

$$
    r = 4166 + \frac{k}{5}.
$$

Note that this means individuals 1, 3 and 5 pay more than they would under the previous scheme while
individuals 2 and 4 will pay less. Thus, this scheme has raised the premiums of low-risk people and lowered
the premiums of high-risk people. One may be fine with this provided the high-risk people are at high risk
due to no fault of their own, e.g. genetic disposition to cancer or natural disasters. If, however, this high risk
is due to carelessness and bad choices that responsible adults would not make, then a scheme like this may
cause controversy: most people probably would not enjoy having to pay higher premiums because other people
are idiots. In essence, this scheme causes low-risk people to subsidize high-risk people.
The limiting behavior of this scheme as $$n$$ grows large is also different: whereas in the previous scheme
the individual premiums converge to the expected costs of the individuals, here the matter is not so clear.
Note first that the expected individual cost is upper-bounded:

$$
    E[Q_j] \leq \sum_{i=1}^m c_i.
$$

Let's denote this bound by $$C$$. We then have

$$
    E[Q] \leq nC.
$$

This yields

$$
    \underset{n \to \infty}{\lim} r = \underset{n \to \infty}{\lim} \frac{E[Q] + k}{n} = \underset{n \to \infty}{\lim} \frac{E[Q]}{n} \leq C.
$$

Thus, depending on the risk associated with newcomers, individual premiums may increase to $$C$$ as more people
are insured by our company. In our hypothetical society, we have $$C = 11700$$, which is significantly higher than
any individual premium $$r_j$$ from our first scheme. In real life, where insurance companies insure against many more
problems than just the three mentioned above, $$C$$ may just as well be infinite.
The end result of using such a scheme may well be that eventually either one of two things has to happen:

1. the insurance company introduces a *numerus clausus* where it limits the number of customers it can have;

2. the company goes bankrupt because no one can pay the high premiums anymore.

From an economic perspective, customers face an actual *dis*incentive to get insurance with a company that adopts such an "equalized" scheme.
To the customer, insurance is only profitable if the benefits outweigh the costs. If the insurance premium is much higher than the customer's
expected cost, then the customer would be better off not having insurance and paying for any eventualities themselves. This defeats the entire
purpose of even having insurance in the first place. So in a sense, the personalized scheme which charges people based on their actual risk
is economically optimal since premiums will converge to the expected costs as $$n$$ grows large. In practice, it will also be socially
preferable to have an individualized insurance scheme instead of an equalized one, since the majority of the population does not lead an
outrageously risky life. Hence, premiums under the former scheme will be cheaper for most people than premiums under the latter.

If the goal is to have as many people insured at as cheap a price as possible, the individualized scheme is the better option.
