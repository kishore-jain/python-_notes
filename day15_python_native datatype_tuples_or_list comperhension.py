Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # native datatypes (list ,tuple, set ,dictionary)
...  
>>> # ----------------------------------------------
>>> 
>>> # tuple
>>> #------
>>> 
>>> # ordered collection of data item
>>> # values are indexed
>>> # values are IMMUTABLE & UNCHANGEABLE
>>> # supports duplicate value
>>> 
>>> # insertion preservation order used
>>> # supports hetrogenous values
>>> 
>>> 
>>> t = ('rk','jeni'10,20,10,'rk')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> t = ('rk','jeni',10,20,10,'rk')
>>> 
>>> type(t)
<class 'tuple'>
>>> t.count('rk')
2
>>> t.index(20)
3
>>> t.find('rk')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t.find('rk')
AttributeError: 'tuple' object has no attribute 'find'
t
('rk', 'jeni', 10, 20, 10, 'rk')


t1 = ('kayal','kani','swetha')

type(t1)
<class 'tuple'>


'rajesh'+'kumar'
'rajeshkumar'

t+t1
('rk', 'jeni', 10, 20, 10, 'rk', 'kayal', 'kani', 'swetha')
# this is called tuple conncatenation

t
('rk', 'jeni', 10, 20, 10, 'rk')
t1
('kayal', 'kani', 'swetha')
t2=t+t1
t
('rk', 'jeni', 10, 20, 10, 'rk')
t1
('kayal', 'kani', 'swetha')
t2
('rk', 'jeni', 10, 20, 10, 'rk', 'kayal', 'kani', 'swetha')


t2 =list(t2)
t2
['rk', 'jeni', 10, 20, 10, 'rk', 'kayal', 'kani', 'swetha']

t2.remove('rk')

t2
['jeni', 10, 20, 10, 'rk', 'kayal', 'kani', 'swetha']

t2.remove('rk')

t2
['jeni', 10, 20, 10, 'kayal', 'kani', 'swetha']

t2 = tuple(t2)

t2
('jeni', 10, 20, 10, 'kayal', 'kani', 'swetha')


# list
# ----

rk = [10,20,30,"alvin","aji","rajesh"]

rk
[10, 20, 30, 'alvin', 'aji', 'rajesh']
rk[0]=kishore
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    rk[0]=kishore
NameError: name 'kishore' is not defined
rk[0]='kishore'
rk
['kishore', 20, 30, 'alvin', 'aji', 'rajesh']
rk.insert(4,'jain')
rk
['kishore', 20, 30, 'alvin', 'jain', 'aji', 'rajesh']


# list comprehension
#-------------------

# allow user to interate over the records of a list with out using looping statements


# iter(),__next__

rk
['kishore', 20, 30, 'alvin', 'jain', 'aji', 'rajesh']

r = iter(rk)  # Here, r is object, rk is list

r
<list_iterator object at 0x000001CC422C29E0>

r.__next__
<method-wrapper '__next__' of list_iterator object at 0x000001CC422C29E0>
r.__next__()
'kishore'
r.__next__()
20
r.__next__()
30
r.__next__()
'alvin'
r.__next__()
'jain'
r.__next__()
'aji'
r.__next__()
'rajesh'
r.__next__()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    r.__next__()
StopIteration

rk
['kishore', 20, 30, 'alvin', 'jain', 'aji', 'rajesh']




for i in rk:
    print(i)

    
kishore
20
30
alvin
jain
aji
rajesh


for k in rk
SyntaxError: incomplete input
for k in rk:
    print(k)

    
kishore
20
30
alvin
jain
aji
rajesh

# task
#-------
