Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# looping statements
# ------------------
# for loop

# while loop

# for loop = (CORM process)- check once runs manytime

for i in range(20):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

# syntax

# for i in range (starting_value,stopping_value,increment)

for i in range(0,10,1)
SyntaxError: incomplete input
for i in range(0,10,1):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(0,10,2):
    print(i)

    
0
2
4
6
8
# print even numbers between 1 to 100

for i in range(0,101,2):
    print(i)

    
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
for i in range(2,101,2):
    print(i,end=' ')

    
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 
# print odd number between 1 to 100

for i in range(0,5,1):
    print(i)

    
0
1
2
3
4
# print number 10 to 1 reverse

for i in range (10,0,-1):
    print(i)

    
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
# print even number 10 to 1

KeyboardInterrupt
KeyboardInterrupt
for i in range (10,0,-2):
    print(i)

    
10
8
6
4
2
# print odd number 10 to 1
for i in range (10,0,-2):
    print(i)

    
10
8
6
4
2

# print 5 tables

# 1 * 5 =5
# 2 * 5 = 10

# 10 * 5 = 50

for i in range (1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
for i in range (1,11):
    print(i,'* 5 =',i*5)

    
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50

for i in range (1,11):
    print('5 * ',i,'=',i*5)

    
5 *  1 = 5
5 *  2 = 10
5 *  3 = 15
5 *  4 = 20
5 *  5 = 25
5 *  6 = 30
5 *  7 = 35
5 *  8 = 40
5 *  9 = 45
5 *  10 = 50



# 7 tables -reverse
for i in range (10,0,-1):
    print('7 * ',i,'=',i*5)

    
7 *  10 = 50
7 *  9 = 45
7 *  8 = 40
7 *  7 = 35
7 *  6 = 30
7 *  5 = 25
7 *  4 = 20
7 *  3 = 15
7 *  2 = 10
7 *  1 = 5
for i in range (10,0,-1):
    print('7 * ',i,'=',i*7)

    
7 *  10 = 70
7 *  9 = 63
7 *  8 = 56
7 *  7 = 49
7 *  6 = 42
7 *  5 = 35
7 *  4 = 28
7 *  3 = 21
7 *  2 = 14
7 *  1 = 7

for i in range'rajesh':
    print(i)
    
SyntaxError: invalid syntax
for i in range 'rajesh':
    print(i)
    
SyntaxError: invalid syntax

for i in 'rajesh':
    print(i)

    
r
a
j
e
s
h
for i in 'rajesh':
    print(i*5)

    
rrrrr
aaaaa
jjjjj
eeeee
sssss
hhhhh
>>> for i in 'rajesh':
...     print(i*5,end=' ')
... 
...     
rrrrr aaaaa jjjjj eeeee sssss hhhhh 
>>> for i in 'rajesh':
...     print(i+5,end=' ')
... 
...     
Traceback (most recent call last):
  File "<pyshell#85>", line 2, in <module>
    print(i+5,end=' ')
TypeError: can only concatenate str (not "int") to str
>>> for i in range (1,11):
...     print('7 / ',i,'=',i/7)
... 
...     
7 /  1 = 0.14285714285714285
7 /  2 = 0.2857142857142857
7 /  3 = 0.42857142857142855
7 /  4 = 0.5714285714285714
7 /  5 = 0.7142857142857143
7 /  6 = 0.8571428571428571
7 /  7 = 1.0
7 /  8 = 1.1428571428571428
7 /  9 = 1.2857142857142858
7 /  10 = 1.4285714285714286
