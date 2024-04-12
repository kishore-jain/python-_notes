Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# flow control statement
# ----------------------

# these statement control the execution flow of a python program

# break
# continue
# pass

for i in range(10):
    print(i,end='')

    
0123456789
for i in range(10):
    print(i,end=' ')

0 1 2 3 4 5 6 7 8 9 
for i in range(10):
    print(i,end=' ')
    if i==5:
        break

    
0 1 2 3 4 5 

for i in range(10):
    print(i,end=' ')
    if i==5:
        break
    print(i)

    
0 0
1 1
2 2
3 3
4 4
5 
for i in range(10):
    if i==5:
        break
    print(i)

    
0
1
2
3
4
# atm debit card -- validity (2/2023 to 6/20300)

# cotinue - it take out the conditional value outside and resumes the exection from next element

for i in range (10):
    print(i,end=' ')

    
0 1 2 3 4 5 6 7 8 9 

for i in range (10):
    if i==5:
        continue
    print(i,end=' ')

    
0 1 2 3 4 6 7 8 9 

for i in range (10):
     print(i,end=' ')
    if i==5:
        continue
    
SyntaxError: unindent does not match any outer indentation level

for i in range (10):
     print(i,end=' ')
    if i==5:
        
SyntaxError: unindent does not match any outer indentation level

for i in range(10):
    print(i,end=' ')
    if i==5:
        continue

    
0 1 2 3 4 5 6 7 8 9 

# pass

# pass does nothingbut simply closes the opened indentationfor i in ra
# pass does nothingbut simply closes the opened indentation

for i in range(5):
    print(i)
    if i==2
    
SyntaxError: incomplete input
for i in range(5):
    print(i)
    if i==2:
        pass

    
0
1
2
3
4
for i in range(5):
    print(i)

    
0
1
2
3
4


# while loop
# -----------

# if checks the condition every singe time and runsthe loop tillthe condition becomes true
# increment / decrement value is mandata iin while loop

a=10

while a>=1:
    print(a)
    a-=1
... 
...     
10
9
8
7
6
5
4
3
2
1
>>> while a>=1:
...     print(a)
...     a+=1
... 
...     
>>> 
>>> while a>=1:
...     print(a)
...     a+=1
... 
...     
>>> 
>>> while a>=1:
...     print(a)
...     a+=5
... 
...     
>>> # task
