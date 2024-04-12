Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# pattern programs using for loop
# -------------------------------

# Right angle triangle
# --------------------

for i in range(1,6):
    for j in range(0,i):
        print(i,end = ' ')
        print()

        
1 
2 
2 
3 
3 
3 
4 
4 
4 
4 
5 
5 
5 
5 
5 
for i in range(1,6):
    for j in range(0,i):
        print(i,end = ' ')
    print()

    
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 













































































































for i in range(1,6):
    for j in range(0,i):
        print(j,end = ' ')
    print()

    
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 
# i ----> outer loop --->row printing --->tells which number to print

# j-------> inner loop----> column printing ---> tells how many times to print



# Right angle triangle -column printing i in range (1,6):
for i in range(1,6):
    for j in range(0,i):
        print(j,end = ' ')
    print()

    
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

# note : both  print function should be given both i and j value

# Right angle triangle -using (*) or any symbol

# -----------------------------------------------
for i in range(1,6):
    for j in range(0,i):
        print('*',end = ' ')
    print()

    
* 
* * 
* * * 
* * * * 
* * * * * 


for i in range(1,20):
    for j in range(0,j):
        print('$',end = ' ')
    print()

    
$ $ $ $ 
$ $ $ 
$ $ 
$ 















>>> for i in range(1,20):
...     for j in range(0,i):
...         print('$',end = ' ')
...     print()
... 
...     
$ 
$ $ 
$ $ $ 
$ $ $ $ 
$ $ $ $ $ 
$ $ $ $ $ $ 
$ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ 
$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ 
>>> 
>>> 
