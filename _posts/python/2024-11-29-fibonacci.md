---
layout: post
code: python
---

~~~{{ page.code }}
def fib(n):
    f,s = 0,1
    if n == 0:
        yield f
    else:
        for _ in range(n):
            yielf f
            f, s = s, f+s 
~~~
