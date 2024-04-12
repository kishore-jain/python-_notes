Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
NameError: name '____________' is not defined

for i in range (1,6):
    for j in range(0,i):
        print(i,end=' ')
    print()

    
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
... 
... for i in range(6,0,-1):
...     for j in range(0,i):
...         print(i,end=' ')
...     print()
... 
...     
... 6 6 6 6 6 6 
... 5 5 5 5 5 
... 4 4 4 4 
... 3 3 3 
... 2 2 
... 1 
... 
... for i in range(6,0,-1):
...     for j in range(0,i):
...         print(j,end=' ')
...     print()
... 
...     
... 0 1 2 3 4 5 
... 0 1 2 3 4 
... 0 1 2 3 
... 0 1 2 
... 0 1 
... 0 
... 
... #irat - uppercase row printing
... #-----------------------------
... 
... for i in range(6,0,-1):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
F F F F F F 
E E E E E 
D D D D 
C C C 
B B 
A 

for i in range(6,0,-1):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

    
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 

#irat - lower case - row printing
#--------------------------------

for i in range(6,0,-1):
    for j in range(0,i):
        print(chr(i+96),end=' ')
    print()

    
f f f f f f 
e e e e e 
d d d d 
c c c 
b b 
a 

#irat - lower case - column printing
#-----------------------------------

for i in range(6,0,-1):
    for j in range(0,i):
        print(chr(i+97),end=' ')
    print()

    
g g g g g g 
f f f f f 
e e e e 
d d d 
c c 
b 
for i in range(6,0,-1):
    for j in range(0,i):
        print(chr(j+95),end=' ')
    print()

    
_ ` a b c d 
_ ` a b c 
_ ` a b 
_ ` a 
_ ` 
_ 
for i in range(6,0,-1):
    for j in range(0,i):
        print(chr(j+97),end=' ')
    print()

    
a b c d e f 
a b c d e 
a b c d 
a b c 
a b 
a 

#left angle triangle
#---------------------

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(i, end=' ')
    print()

    
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 

#lat - number column priting
#--------------------------

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(j, end=' ')
    print()

    
        2 
      3 3 
    4 4 4 
  5 5 5 5 
5 5 5 5 5 
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(k, end=' ')
    print()

    
        0 
      0 1 
    0 1 2 
  0 1 2 3 
0 1 2 3 4 

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,1):
        print(chr(k+64),end=' ')
    print()

    
        @ 
      @ 
    @ 
  @ 
@ 
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,1):
        print(chr(i+64),end=' ')
    print()

    
        A 
      B 
    C 
  D 
E 
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
        A 
      B B 
    C C C 
  D D D D
E E E E E 


for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(j+65),end=' ')
    print()

    
        C 
      D D 
    E E E 
  F F F F 
F F F F F 

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(k+65),end=' ')
    print()

    
        A 
      A B 
    A B C 
  A B C D 
A B C D E 

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(i+95),end=' ')
    print()

    
        ` 
      a a 
    b b b 
  c c c c 
d d d d d 

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(k+97),end=' ')
    print()

    
        a 
      a b 
    a b c 
  a b c d 
a b c d e 
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print('*',end=' ')
    print()

    
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

for i in range(1,6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(j+64),end=' ')
    print()

    
    B 
   C C 
  D D D 
 E E E E 
E E E E E 
for i in range(1,6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
    A 
   B B 
  C C C 
 D D D D 
E E E E E 
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
E E E E E 
  D D D D 
    C C C 
      B B 
        A 

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
E E E E E 
 D D D D 
  C C C 
   B B 
    A 
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end='')
    for k in range(0,i):
        print(chr(i+64),end='')
    print()

    
EEEEE
DDDD
CCC
BB
