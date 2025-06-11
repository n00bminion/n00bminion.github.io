---
layout: post
code: MASU5050
usemathjax: true
---

This is another basic topic... Not much to say, mostly straight forward but links back to the knowledge from sets 🧠


***
<br>

### Functions

A function is $ f : A \rightarrow B $ is a rule which associate each $x$ member of set A which we call **domain** of $f$ (we also say $f$ is defined on A) to a **unique** $y$ value in the set B which we call **codomain** of $f$.

We then write 

$$ y = f(x) $$ 

Where we call $f(x)$ the value of $f$ at $x$. The set of values of $f$ as $x$ takes all the values in A is called the range of $f$. The range of the $f$ is a subset of the codomain of $f$.

For some functions, the input might not make sense and/or is not defined. $f(x)= \tfrac{1}{x}$ is one where $x=0$ is possible. We then say function is not defined at $x = 0$. Since the functions works for all real numbers, we can say that the "function $ f $ is defined by $ f(x) = \tfrac{1}{x}, x \ne 0$" or "function $$f : \mathbb{R}\backslash \{0\} \rightarrow \mathbb{R}$$ is defined by $f(x) = \tfrac{1}{x}$". 

Note that $$ \mathbb{R}\backslash \{0\} $$ denote real numbers excluding 0

<br>

### Even & Odd Functions

$f$ is an **even** function if $f(x) = f(-x)$

$f$ is an **odd** function if $f(x) = -f(-x) \implies -f(x) = f(-x)$

Note that all even functions have a symmetry about the $y$-axis (reflected by the $y$-axis) whereas the odd functions will have a rotational symmetry of order 2. This effectively mean you just have to rotate it by 90 degrees twice to get back to the same graph.

An example of even function is $ f(x) = x^2 $. Both positive and negative $x$ maps to the same positive $y$ value. For the odd function, we can use $ f(x) = x $, where positive $x$ maps to positive $y$ only and vice versa. This satisfies the condition above $f(x) = -f(-x)$.

<br>

### Periodic Functions

$f$ is a **periodic** function if $f(x) = f(x+a)$ where $a$ is the period of $f$.

Usually periodic functions are some sort of trignometric functions.

<br>

### Polynomials Functions

The general polynomial of degree $n$ in $x$ can be written as

$$ y = f(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + ... +  a_1x^1 + a_0 \nonumber $$

where $a_n, a_{n-2}, a_{n-3} ... a_1, a $ are numbers or coefficients and $a_n \ne 0$. The degree of the polynomial is the highest power of $x$.

A popular polynomial function is the **quadratic** function, where it is a polynomial of degree 2. Rearranging the polynomial equation can show the position and shape of the graph.

$$ f(x) = ax^2 + bx + c \nonumber $$ 

Dividing all terms by $a$ and complete the square

$$ f(x) = a\left(x^2 + \frac{b}{a}x + \frac{c}{a}\right) \implies a\left(\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} + \frac{c}{a}\right) \nonumber $$
 
Finally group the non $x$ terms in the bracket together

$$ a\left( \left(x + \frac{b}{2a}\right)^2 - \frac{b^2-4ac}{4a^2} \right) \nonumber $$


The graph of the $f(x)$ is thus obtained from $y=x^2$. This is shifted to the right by $-\frac{b}{2a}$, shifted downward by $\frac{b^2-4ac}{4a^2}$ and then scaled by $a$. Note that a negative value of $a$ will flip the graph upside down (reflection across the x axis) along with any scaling by $a$


There's some extra stuff about polynomials [here]({% post_url /maths-method-for-stats/2024-10-03-basics-maths %})

I can't be bothered to draw graphs to show the transformation but here's a link of what it looks like [visually](https://mathbitsnotebook.com/Algebra1/FunctionGraphs/FNGTransformationFunctions.html)
<br>

### Rational Functions

Rational function $f$ is defined as

$$ f(x) = \frac{p(x)}{q(x)} \nonumber $$

where both $p$ and $q$ are polynomials. We need to be careful to exclude points where $q(x)$ is zero from the domain of both $p$ and $q$.

An example of this is we ignore 0 from all real values in the domain like below and the range of $f$ is R

$$ f: \mathbb{R} \backslash \{0\} \rightarrow \mathbb{R} \space defined \space by \space f(x) = \frac{1}{x} \nonumber$$

Or any value that will make the denominator equal to zero. In this case, we ignore 1 from the domain and the range of $f$ is R

$$ f: \mathbb{R} \backslash \{1\} \rightarrow \mathbb{R} \space defined \space by \space f(x) = \frac{x^2}{x^3-1} \nonumber$$


<br>

### Trignometric Functions

Before going into trignometric functions, we need to define radian and what it is. (This is a definition from the text book)

A radian is the angle subtended at the center of a circle by an arc which is the same length as the radius (subtended is a word I can never remember but it means opposite of something so in this context it is the angle at the center of of the circle which is opposite the arc, where the arc is a part of the circumference and this arc has the same length as the radius). If we have a unit circle where the radius is one, then the arc has a length of 1. 

We know formula of circumference of circle is $2\pi r$ which then equates to 360 degrees. Thus on a unit circle:

$$ 2\pi \space radian = 360^\circ \nonumber $$

$$ \pi \space radian = 180^\circ \nonumber $$

$$ \pi/2 \space radian = 90^\circ \nonumber $$

And in general, using the below, we can convert between radian and degree.

$$ 1 \space radian = \frac{180^\circ}{\pi}  \nonumber  $$

For example,  

$$ \frac{\pi}{3} \space radian \Rightarrow \frac{\pi}{3} . \frac{180^\circ}{\pi} = 60^\circ \nonumber $$

Trignometric functions are functions of angles which are measured in radians. If we see the below unit circle where angle $t$ and the point $(x,y)$ on the circumference of the circle. We can deduce that that $cos(t)= x$ and $sin(t) = y$. 

![Image](/assets/images/unit_circle.png){:height="50%" width="50%" style="display: block; margin: 0 auto" }

Along with this, we also have other trignometric identities:

$$ tan(t) = \frac{sin(t)}{cos(t)};\space cot(x) = \frac{cos(t)}{sin(t)};\space sec(x) =  \frac{1}{cos(t)};\space cosec(x) =  \frac{1}{sin(t)} \nonumber$$

#### Sine Rule

From the above functions, we also have the sine rule. This is given as 

$$ \frac{sin A}{a} = \frac{sin B}{b} =\frac{sin C}{c} \nonumber $$

or 

$$ \frac{a}{sin A} = \frac{b}{sin B} =\frac{c}{sin C} \nonumber $$

We can derive this by draw the line $h_B$ which create a right angle with AC from B like below.

![Image](/assets/images/sine_rule.png){:height="50%" width="50%" style="display: block; margin: 0 auto" }

Let write out all the bits we know

$$ sin A = \frac{h_B}{c}; \space sin C = \frac{h_B}{a} \Rightarrow cSinA = h_B; \space aSinC = h_B \nonumber$$

Since both are equal to $h_b$, we can write

$$ cSinA = aSinC  \Rightarrow \frac{SinA}{a} = \frac{SinC}{c} \Rightarrow \frac{a}{sinA} = \frac{c}{sinC} \nonumber  $$

In the case above, we drew line $h_B$ but we could also draw line $h_C$ from C and making a right angle with AB in a similar fashion like $h_B$ (or $h_A$ from A to BC). Going through the same logical reasoning, we can see that for $h_C$,

$$ bSinA = aSinB  \Rightarrow \frac{SinB}{b} = \frac{SinA}{a} \Rightarrow \frac{a}{sinA} = \frac{b}{sinB} \nonumber  $$

or for $h_A$,

$$ bSinC = cSinB  \Rightarrow \frac{SinB}{b} = \frac{SinC}{c} \Rightarrow \frac{c}{sinC} = \frac{b}{sinB} \nonumber  $$

From the above 3 results, we can very easily derive sine rule.

#### Cosine Rule

Next is cosine rule, this is given as:

$$ a^2 = b^2 + c^2 - 2bc \space cos A  \nonumber $$

Using the same triangle above, if we set the distance $x$ to be from A to where $h_B$ meets B and therefore $h_B$ to C is $b-x$

We have the below:

$$ cosA = \frac{x}{c} \implies c \space cosA = x \nonumber $$

also applying the Pythagoras theorem to both inner right angle triangles, we get

$$ c^2 = h_B^2 + x^2 \space \And \space a^2 = h_B^2 + (b-x)^2 \nonumber $$

rearrange to remove the $h_B$, setting everything equals to $a^2$ and then expands the bracket

$$ a^2 = (b-x)^2 + (c^2 - x^2) \implies b^2-2bx+x^2 + c^2 - x^2 \nonumber $$

finally, cancelling the $x^2$ terms and replacing $x$ term with the $c \space cosA$

$$ a^2 = b^2-2bx + c^2 \implies b^2-2bc \space cosA + c^2 \implies b^2 + c^2 -2bc \space cosA \nonumber $$

You can do the same with side c and side b to get the results

$$ c^2 = b^2 + a^2 -2ba \space cosC \space \And \space b^2 = c^2 + a^2 -2ca \space cosB; \nonumber $$


<br>

### Composite & Inverse Functions


<br>

### Indicator Functions

