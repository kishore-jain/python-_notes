Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# functions in python
# -------------------

# self contained module
# organised collection of meaningful instruction to do a specific task
# reuseable code template

# example:

def add(a,b):
    return a+b

# def - keyword (def means define [create])
# add - user defined function
# a,b - parameteres (place holder or value container)
# return - keyword

# what comes after def always called as function and respresent in paramaters

add(3,50)
53
add(20+40)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    add(20+40)
TypeError: add() missing 1 required positional argument: 'b'

add(20,30)
50

# function means reusable code template
>>> # function means reusable instruction template
>>> # function means self contained module
>>> # function means reusable programming instructions
>>> # function usually returns PROCESSED OUTPUT VALUE as end result
>>> # function returns end result only when it get called
>>> 
>>> 20,42
(20, 42)
>>> 
>>> add(20,10)
30
>>> 
>>> # function usually provides NAME SPACES
>>> 
>>> def mul(a,b):
...     return a*b
... 
>>> def sub(a,b):
...     return a-b
... 
>>> add(40,50)
90
>>> mul(40,50)
2000
>>> sub(40,50)
-10
>>> 
>>> # each function has a unique behaviour

