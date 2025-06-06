---
layout: post
code: MASU5051
usemathjax: true
---
 
some text

***

### Sample Space & Events

A sample space is the set of all possible outcomes from an experiment. This is denoted with $ \mathbb{S} $

An event space is subset of the sample space or might just be a single value. This also means all of the events in the event space must also be in the sample space.

For dice roll, the sample space is 

$$ \mathbb{S} = \{1,2,3,4,5,6\} \nonumber$$

For coin toss, the sample space is 

$$ \mathbb{S} = \{H,T\} \nonumber$$

For more info on sets, you can find it **[here]({% post_url /maths-method-for-stats/2024-10-04-sets %})**

In cases where we have multiple multiple variables for the events, we will need to define both variables

For rolling 2 dices simultaneously, the sample space and event space for sum total the 2 dice is 7 is

Sample space:

$$ \mathbb{S} = \{ (x,y) | x=\{1,2,3...6\}, y=\{1,2,3...6\} \} \nonumber$$

Events where you have 2 dices totaling 7 are:

$$ \mathbb{E} = \{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1) \} \nonumber$$

$$ \mathbb{E} = \{(z,7-z) | z = \{1,2,3...6\} \} \nonumber$$

<br>

### Partition

A partition $$ \{ E_1, E_2, E_3... \} $$ of the set $ \mathbb{S} $ is a set of subsets of $ \mathbb{S} $ such that every element of $ \mathbb{S} $ appears in exactly one of the subsets $ \{ E_1, E_2, E_3... \} $

If $$ \{ E_1, E_2 \} $$ is a partition of $ \mathbb{S} $ where:

$$  E_1 = \{1,2\} \nonumber$$

$$  E_2 = \{3,4\} \nonumber$$

Then $$ \mathbb{S} = \{ 1,2,3,4 \} \nonumber$$

<br>

### Classical Probabilities

This assumes every outcome in the sample space is equally likely so the probability of any event is is calculated as the number of outcomes in which event occur divided by all the possible outcomes which is the sample space

$$ \mathbb{P}(A) = \frac{no. \ of \ elements \ in \ A}{no. \ of \ elements \ in \ \mathbb{S}} \nonumber $$

<br>

### Relative Probabilities

Where we can't accomodate events which are not equally likely, we can imagine the experiment being repeated many times.

$$ \mathbb{P}(A) = \frac{no. \ of \ times \ A \ occured }{no. \ of \ time \ experiement \ is \ repeated } \nonumber $$

We then assume that the relative frequency settle down to a fixed limit as number of repeat tends to infinity

<br>

### Subjective Probabilities

There are many cases where we can't repeat the experiment so we allow the individual to assume their probabilities based on their preferemces and experiences.

<br>

### Venn Diagrams

Given a sample space ${\mathbb{S}}$ and 2 events A and B, the interactions between the 2 events are:

<br>

$A \cup B $ where the shaded region is A, B or both

![Image](/assets/images/set_union.png){:height="50%" width="50%"}

<br>


$A \cap B $ where the shaded region is only both A and B 

![Image](/assets/images/set_intersect.png){:height="50%" width="50%"}

<br>

$ A \cap B = \emptyset \nonumber$ where the two events A and B do not intersect and are mutually exclusive. This also results in the empty set $\emptyset$ where there are no elements in the set

![Image](/assets/images/set_mutually_exclusive.png){:height="50%" width="50%"}

<br>

$ \overline A $ is the complement of A where it showfs A not occurring i.e. everything not A

![Image](/assets/images/set_complement.png){:height="50%" width="50%"}

<br>

$ A/B $ or $ A \cap \overline B $ where all things in A but nothing in B. This is the set difference between A and B

![Image](/assets/images/set_difference.png){:height="50%" width="50%"}

