Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# lambda functions
# ----------------

# onetime function
# nameless function
# inline function

def bot(a,b,c):
    if a>b and a>c:
        print(a,'is bigger')
    elif b>c:
        print(b,'is bigger')
    else:
        print(c,'is bigger)
              
SyntaxError: incomplete input

def bot(a,b,c):
    if a>b and a>c:
        print(a,'is bigger')
    elif b>c:
        print(b,'is bigger')
    else:
        print(c,'is bigger')

        
bot(23,45,85)
85 is bigger

# lambda function rules
# ---------------------

# do not use def keyword, instead use lambda keyword
# do not use print function
# do not use elif keyword

# NOTE : in lambda function if condition is ture it executes left side , if conditon is false it executes right side of the function

big = lambda a,b,c: a if a>b and a>c else b if b>c else c

big(12,54,26)
54

# lambda supporting functions
# ---------------------------

# map
# filter
# reduce

rk=[1,2,3,4,5,6,7,8,9,10]

# map creates a new list with the help of existing list along side lambda function

rk*5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in rk:
    print(i*5)

    
5
10
15
20
25
30
35
40
45
50

m = list(map(lambda a: a*5, rk))

m
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# filter -  returns a new filtered list of values from existing list

rk
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = list(filter(lambda a: a%2==0, rk))

f
[2, 4, 6, 8, 10]

f = list(filter(lambda a: a%2==1, rk))
f
[1, 3, 5, 7, 9]

f = list(filter(lambda a: a*5, rk))
f
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = list(filter(lambda a: a*5!=0, rk))
f
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


f = list(filter(lambda a: a%2==1, m))
f
[5, 15, 25, 35, 45]
>>> 
>>> f = list(filter(lambda a: a%2==0, m))
>>> f
[10, 20, 30, 40, 50]
>>> 
>>> m1 = list(map(lambda a: a%2==0, m))
>>> m1
[False, True, False, True, False, True, False, True, False, True]
>>> 
>>> m1 = list(map(lambda a: a%2, m))
>>> m1
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
>>> 
>>> m1 = list(map(lambda a: a/2, m))
>>> m1
[2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0]
>>> 
>>> 
>>> # reduce
>>> # ------
>>> 
>>> rk
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> from functools import reduce
>>> 
>>> r = reduce(lambda a,b: a+b, rk)
>>> r
55
>>> 
>>> sum(rk)
55
>>> 
