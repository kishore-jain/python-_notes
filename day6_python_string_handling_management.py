Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# string handing management
#---------------------------

# category1 - string operations
# category2 - string methods
# category3 - string supporting functions

# category1- string operations
#-----------------------------

# indexing = (getting particular character from a string using index value)
# slicing = (getting a portion of value from a string using starting value & stoping value)
# ranging = (similar to slicing with anyone value following by :)

name ='elangovan'

name[0]
'e'
name[1]
'l'
name[2]
'a'
name[5]
'o'
name[8]
'n'
# this is called positive indexi

# positive indexing is called as string traversing

name[-1]
'n'
name[-2]
'a'
name[-3]
'v'
name[-5]
'g'
name[-7]
'a'
name[-9]
'e'
name[-11]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name[-11]
IndexError: string index out of range

# this is negative indexing also called as back tracking / back traversing

#2. slicing
#---------

name
'elangovan'


name[0:5]
'elang'
name[0:6]
'elango'

#note: every time python should print n-1 value in stopping value
# ex: [0:5] means prints value (0,1,2,3,4)- not prints value 5


name[4:7]
'gov'
name[4:6]
'go'
# van

name[6:9]
'van'
name[9]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    name[9]
IndexError: string index out of range

name[6:9]
'van'

#lang

name
'elangovan'

name[1:5]
'lang'
name
'elangovan'
name='alvina'

# alvi

name[0:4]
'alvi'
# vin

name[2:5]
'vin'
# here, 2 is starting value & 5 is stopping value

# this process is called positive slicing

# [6:9] [1:5] [0:4] [2:5]

# note: starting value is always smaller and stopping value is always higher

name
'alvina'


name[0:4]
'alvi'
name[4:0]
''

# negative slicing
#-----------------

name
'alvina'

name[-1]
'a'
name[-2]
'n'
name[-3]
'i'
name[-4]
'v'
name[-5]
'l'
name[-6]
'a'

name[-6:-3]
'alv'
name[-6:-2]
'alvi'
name[-2:2]
''
# -6 is smaller than -2
-5000000<-1
True
name[-6:]
'alvina'
name
'alvina'

# alvin

name[-6:-1]
'alvin'

name[-6:0]
''
name[0:-6]
''
name[-6:]
'alvina'

>>> 
>>> name='muzaaa'
>>> 
>>> name[::-1]
'aaazum'
>>> 
>>> 
>>> name[0]
'm'
>>> name[3]
'a'
>>> name[0],[3]
('m', [3])
>>> name[0],name[3]
('m', 'a')
>>> 
>>> # ranging
>>> #-------
>>> name='rajesh kumar'
>>> 
>>> name[6]
' '
>>> name[6:]
' kumar'
>>> name[9:]
'mar'
>>> name[:6]
'rajesh'
>>> name[6:]
' kumar'
