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

A polynomial in $x$, $p(x)$ is an expression of the form below where the degree of polynomial is $n$, the leading coefficient is $a_n$ along with the leading term being $a_nx^n$. The *constant* term is $a_0$ which mean this does not have an $x$ associated with it.

$$ p(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + ... +  a_1x^1 + a_0 \nonumber $$

The Factor Theorem then states that

Let $p(x)$ be a polynomial of $x$ as described above where $a_n \ne 0$.

1. If $a_n = 1$ then $p(a) = 0$ if $(x-a)$ is a factor of $p(x)$
2. If $a_n \neq 1$ then $(bx-a)$ is a factor of $p(x)$ if $p(\frac{b}{a})=0$

What this means in practice is when we find factors of the polynomial $p(x)$, the factor is of either form $(x-a)$ or $(bx-a)$ where a and b are integers and we evaluate $p(a)$ or $p(\frac{b}{a})$ for all $a$ which are factors of the constant term and all b which are factors of the leading coefficient $a_n$. 

For example, if $f(x) = 2x^3 + 6x^2 + x + 3$, we know one of the factor must have a root that is a factor of the constant term 3. Trying $f(-3)$ and this gives so $x+3$ is a factor. We can get the other root by carrying out long division.

$$
\require{enclose}
\begin{array}{rll}
    2x^2 + 1 \\
    x+3 \enclose{longdiv}{2x^3 + 6x^2 + x + 3}\kern-.2ex \\
    \underline{2x^3 + 6x^2\phantom{0000000}} \\
    x + 3 \\
    \underline{x + 3 }  \\
    \phantom{00}0
  \end{array}

  \nonumber
$$
   
<br>

### Completing The Square

This is a technique to use on $2^{nd}$ degree expression or quadratic expression to find factors. The technique involves rewriting the quadratic as a sum of squared linear terms and a constant.

From above in the *Polynomials* section, we can see that $(x+a)^2 = x^2 + 2ax + a^2$. This can be rewriten as:

$$ (x+a)^2 - a^2 = x^2 + 2ax \nonumber $$

Note that the middle term in the expanded quadratic expression is $2ax$ and thus we can deduce $a$ is by dividing this term by 2. I always forget this bit and get a bit confused for some reason but it the most important part. It then just becomes an exercise of plugging in the numbers.

For example, we have:

$$x^2 + 6x + 10 \nonumber$$ 

We can replace the $x^2 + 6x$ part with $(x+3)^2 - 3^2$ using the above to give

$$(x+3)^2 - 3^2 + 10 \implies (x+3)^2 - 9 + 10 \implies (x+3)^2 + 1 \nonumber $$

When we have a leading coefficient that's not 1, we can take it out as a factor...

$$ 2x^2 + 6x + 10 \implies 2(x^2 + 3x + 5) \nonumber $$ 

$$ 2((x + \frac{3}{2})^2 - (\frac{3}{2})^2 + 5) \implies 2((x + \frac{3}{2})^2 - \frac{9}{4} + 5) \implies 2(x + \frac{3}{2})^2 - \frac{9}{2} + 10 \nonumber $$ 

$$ 2(x + \frac{3}{2})^2 + \frac{11}{2} \nonumber $$

In instances where there are terms in y as well (like when it's equation of a circle)...

$$ x^2 + y^2 + 4x - 2y + 3 \nonumber $$

Let's put all the x and y terms together first and then carry out completing the to the x and y terms seperately

$$ (x^2 + 4x) + (y^2 - 2y) + 3 \implies (x+2)^2 - 4 + (y-1)^2 - 1 + 3 \implies (x+2)^2 + (y-1)^2 - 2 \nonumber $$

Or we can even have:

$$ x^2 + 2xy - 5 \implies (x+y)^2 - y^2 - 5 \nonumber $$


<br>