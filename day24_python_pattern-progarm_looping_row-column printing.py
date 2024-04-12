Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# rat -number -row printing

for i in range(1,6):
    for j in range(0,i):
        print (j,end=' ')
    print()

    
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 
for i in range(1,6):
    for j in range(0,i):
        print (i,end=' ')
    print()

    
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

# rat -number -column print
for i in range(1,6):
    for j in range(0,i):
        print (j,end=' ')
    print()

    
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

# rat -ster printing
for i in range(1,6):
    for j in range(0,i):
        print ('*',end=' ')
    print()

    
* 
* * 
* * * 
* * * * 
* * * * * 

chr(65)
'A'
for i in range(1,6):
    for j in range(0,i):
        print (i+64,end=' ')
    print()

    
65 
66 66 
67 67 67 
68 68 68 68 
69 69 69 69 69 

# rat -uppercase row printing

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64,end=' '))
    print()

    
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    print(chr(i+64,end=' '))
TypeError: chr() takes no keyword arguments
for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64,end=' ')
    print()
              
SyntaxError: '(' was never closed

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

              
A 
B B 
C C C 
D D D D 
E E E E E 
# rat -uppercase column printing
              
for i in range(1,6):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

              
A 
A B 
A B C 
A B C D 
A B C D E 
# rat -lowercase row printing
              

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+97),end=' ')
    print()

              
b 
c c 
d d d 
e e e e 
f f f f f 

# rat -lowercase cloumn printing
              
for i in range(1,6):
    for j in range(0,i):
        print(chr(j+97),end=' ')
    print()

              
a 
a b 
a b c 
a b c d 
a b c d e 


name ='alvina'
              
name[0]
              
'a'
name[1]
              
'l'
name[2]
              
'v'
name[3]
              
'i'
name[4]
              
'n'
name[5]
              
'a'
name[6]
              
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name[6]
IndexError: string index out of range
# rat -name-row-printing
              
for i in range(0,len(name)):
    for j in range(0,i+1):
            print(name[i],end=' ')
        print()
              
SyntaxError: unindent does not match any outer indentation level
for i in range(0,len(name)):
    for j in range(0,i+1):
            print(name[i],end=' ')
    print()

              
a 
l l 
v v v 
i i i i 
n n n n n 
a a a a a a 
# rat -name-column-printing
              
for i in range(0,len(name)):
    for j in range(0,i+1):
            print(name[j],end=' ')
    print()

              
a 
a l 
a l v 
a l v i 
a l v i n 
a l v i n a 
#rat -name-row-printing
              
name='badass ma leodas maa'
              
name
              
'badass ma leodas maa'
for i in range(0,len(name)):
    for j in range(0,i+1):
            print(name[i],end=' ')
    print()

              
b 
a a 
d d d 
a a a a 
s s s s s 
s s s s s s 
              
m m m m m m m m 
a a a a a a a a a 
                    
l l l l l l l l l l l 
e e e e e e e e e e e e 
o o o o o o o o o o o o o 
d d d d d d d d d d d d d d 
a a a a a a a a a a a a a a a 
s s s s s s s s s s s s s s s s 
                                  
m m m m m m m m m m m m m m m m m m 
a a a a a a a a a a a a a a a a a a a 
a a a a a a a a a a a a a a a a a a a a 
# rat -name-column-printing
for i in range(0,len(name)):
    for j in range(0,i+1):
            print(name[j],end=' ')
    print()

              
b 
b a 
b a d 
b a d a 
b a d a s 
b a d a s s 
b a d a s s   
b a d a s s   m 
b a d a s s   m a 
b a d a s s   m a   
b a d a s s   m a   l 
b a d a s s   m a   l e 
b a d a s s   m a   l e o 
b a d a s s   m a   l e o d 
b a d a s s   m a   l e o d a 
b a d a s s   m a   l e o d a s 
b a d a s s   m a   l e o d a s   
b a d a s s   m a   l e o d a s   m 
b a d a s s   m a   l e o d a s   m a 
b a d a s s   m a   l e o d a s   m a a 
 name='jacob mason andrew rajesh kumar Andikalai'
              
SyntaxError: unexpected indent
name
              
'badass ma leodas maa'
>>> name='jacob mason andrew rajesh kumar Andikalai'
...               
>>> name
...               
'jacob mason andrew rajesh kumar Andikalai'
>>> #rat -name-row-printing
...               
>>> for i in range(0,len(name)):
...     for j in range(0,i+1):
...             print(name[i],end=' ')
...     print()
... 
...               
j 
a a 
c c c 
o o o o 
b b b b b 
            
m m m m m m m 
a a a a a a a a 
s s s s s s s s s 
o o o o o o o o o o 
n n n n n n n n n n n 
                        
a a a a a a a a a a a a a 
n n n n n n n n n n n n n n 
d d d d d d d d d d d d d d d 
r r r r r r r r r r r r r r r r 
e e e e e e e e e e e e e e e e e 
w w w w w w w w w w w w w w w w w w 
                                      
r r r r r r r r r r r r r r r r r r r r 
a a a a a a a a a a a a a a a a a a a a a 
j j j j j j j j j j j j j j j j j j j j j j 
e e e e e e e e e e e e e e e e e e e e e e e 
s s s s s s s s s s s s s s s s s s s s s s s s 
h h h h h h h h h h h h h h h h h h h h h h h h h 
                                                    
k k k k k k k k k k k k k k k k k k k k k k k k k k k 
u u u u u u u u u u u u u u u u u u u u u u u u u u u u 
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 
a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r 
                                                                
A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 
n n n n n n n n n n n n n n n n n n n n n n n n n n n n n n n n n n 
d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i 
k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k 
a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l 
a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i 
# rat -name-column-printing
for i in range(0,len(name)):
    for j in range(0,i+1):
            print(name[j],end=' ')
    print()

              
j 
j a 
j a c 
j a c o 
j a c o b 
j a c o b   
j a c o b   m 
j a c o b   m a 
j a c o b   m a s 
j a c o b   m a s o 
j a c o b   m a s o n 
j a c o b   m a s o n   
j a c o b   m a s o n   a 
j a c o b   m a s o n   a n 
j a c o b   m a s o n   a n d 
j a c o b   m a s o n   a n d r 
j a c o b   m a s o n   a n d r e 
j a c o b   m a s o n   a n d r e w 
j a c o b   m a s o n   a n d r e w   
j a c o b   m a s o n   a n d r e w   r 
j a c o b   m a s o n   a n d r e w   r a 
j a c o b   m a s o n   a n d r e w   r a j 
j a c o b   m a s o n   a n d r e w   r a j e 
j a c o b   m a s o n   a n d r e w   r a j e s 
j a c o b   m a s o n   a n d r e w   r a j e s h 
j a c o b   m a s o n   a n d r e w   r a j e s h   
j a c o b   m a s o n   a n d r e w   r a j e s h   k 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n d 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n d i 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n d i k 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n d i k a 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n d i k a l 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n d i k a l a 
j a c o b   m a s o n   a n d r e w   r a j e s h   k u m a r   A n d i k a l a i 
