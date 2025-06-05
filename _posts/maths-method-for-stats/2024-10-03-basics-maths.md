---
layout: post
code: MASU5050
usemathjax: true
---

Starting off with the basics… This page builds the basics that will be useful but I didn't fancy creating a page per topic so I'm shoving everything in here instead. 

A lot of this stuff are super easy but it's always useful to remind myself. More often than not, I have forgotten or will try and work out through first principle.

***
<br>

### Differences Of Two Squares

$$ (a+b)(a-b) = a^2-b^2 \nonumber $$

You can check the results by expanding the brackets but noticed that both a and b multiplies each other once but are of the opposite sign so they cancel out leaving the $a^2$ and $b^2$ 

A slightly more complicated example is the below but we can still use differences of two squares to work out it. 

$$ (a+b)^2 - (a-b)^2 = ((a+b)+(a-b))((a+b)-(a-b)) \nonumber $$

$$ = 2a * 2b \nonumber $$

$$ = 4ab \nonumber $$


### Polynomials 

We should know how the $(a+b)^n$ where is $n$ an integer, expands to and what each of the term coefficients are.

The coefficients of each of the x terms come from the Pascal's triangle and can be denote using the $\binom{n}{r}$ notation, which comes shows the number of ways to choose $r$ from $n$ without replacement. 

$$ 
1 \\ 
1 \hspace{2mm} 1 \\ 
1 \hspace{2mm} 2 \hspace{2mm} 1 \\ 
1 \hspace{2mm} 3 \hspace{2mm} 3 \hspace{2mm} 1 \\ 
1 \hspace{2mm} 4 \hspace{2mm} \hspace{2mm} 6 \hspace{2mm} 4 \hspace{2mm} 1 \\
1 \hspace{2mm} 5 \hspace{2mm} \hspace{2mm} 10 \hspace{2mm} 10 \hspace{2mm} 5 \hspace{2mm} 1 \\
\vdots
\nonumber $$

The term themselves are much easier to see, using the Pascal's triangle, we can see that the terms will be of the form $a^{n-r} b^{r}$ where $r$ is the position entry and $n$ is the row in the Pascal triangle if we start our counting from the $0^{th}$ position and row. 

For the first few powers, we have

$$(a+b)^2 = a^2 + 2ab + b^2 \nonumber$$

$$(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 \nonumber$$

$$\vdots \nonumber$$

$$(a+b)^n = \binom{n}{0} a^nb^0 + \binom{n}{1} a^{n-1}b^1 + \binom{n}{2} a^{n-2}b^2 + \dots + \binom{n}{n-r-1} a^{n-r-1}b^{r-1} + \binom{n}{n-r} a^{n-r}b^{r} \nonumber$$ 

<br>

### Power & Indices

This part shows the notation when a number is multiplied by itself a number of times

$$ x_1.x_2.x_3.x_4...x_n = x^n \nonumber $$

We can then define the below

$$ x^1 = x \nonumber $$

And thus 

$$ x^0 = 1 \nonumber $$

You can get to this result since to go from $x^n$ to $x^{n-1}$, we divide by $x$. We can apply the same to $ x^1 $

Applying the same logic, we can show that negative power would be

$$ x^{-n} = \frac{1}{x^n} \nonumber $$

When we combine two power as per below, we can see that 

$$ x_1.x_2.x_3.x_4 = x^4 \nonumber $$

and

$$ x_1.x_2.x_3 = x^3  \nonumber $$
 
thus

$$ x^3 * x^4 = (x_1.x_2.x_3) * (x_1.x_2.x_3.x_4) \nonumber $$

$$ x^3 * x^4 = x^7 \nonumber $$

More generally, this becomes

$$ x^m * x^n = x^{m+n} \nonumber $$

and 

$$ (x^{m})^n = x^{mn} \nonumber $$

Using the above, we can derive the definition for fractional indices to show that 

If 

$$(x^\frac{1}{2})^2 = x^1 \nonumber $$ 

then 

$$x^\frac{1}{2} = \sqrt{x} \nonumber $$ 

Thus we can write 

$$ x^\frac{m}{n} = \sqrt[n]{x^m} = (\sqrt[n]{x})^m  \nonumber $$ 

Once we have number under roots, these roots can be further simplied, sometimes into whole numbers but other time into **surds** which cannot be resolved into whole numbers like the below example. 

$$ \sqrt{20} = \sqrt{4*5} = \sqrt{4}*\sqrt{5} = 2\sqrt{5}  \nonumber $$


<br>

### Fraction & Rationalising

We can only add/subtract fractions with same denominator. The below gives an example of how we can do this...

$$ \frac{a}{b(a+b)} - \frac{b}{a(a+b)} = \frac{a^2-b^2}{ab(a+b)} \nonumber $$

Using differences of two squares and cancelling out the $(a+b)$

$$ \frac{(a-b)(a+b)}{ab(a+b)} = \frac{(a-b)}{ab} \nonumber $$

We can seperate the fraction out again

$$ \frac{a}{ab} - \frac{b}{ab} = \frac{1}{b} - \frac{1}{a} \nonumber $$


<br>

### Factorising

To factorise is to write the expression as a product of factors. This helps to simplify and solving equations.

We can use **Factor Theorem** to spot the factors for an expression but first we need to know about polynomials. 

A polynomial in $x$, $p(x)$ is an expresson of the form below where the degree of polynomial is $n$, the leading coefficient is $a_n$ along with the leading term being $a_nx^n$. The *constant* term is $a_0$ which mean this does not have an $x$ associated with it.

$$ p(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + ... +  a_1x^1 + a_0 \nonumber $$

The Factor Theorem then states that

Let $p(x)$ be a polynomial of $x$ as described above where $a_n \ne 0$.

1. If $a_n = 1$ then 

<br>

### Completing The Square


<br>