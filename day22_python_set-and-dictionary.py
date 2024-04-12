Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# set

a={1,2,3,4,5}
b={8,7,6,5,4}

a.symmetric_difference(b)
{1, 2, 3, 6, 7, 8}
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
a.intersection(b)
{4, 5}
#symmetric different which tells about skips common things in both set
# reverse process of intersection is symmetric difference
a.isdisjoint(b)
False
# conjoint mean connection b/w A and B false =disjoin
# disjoint mean no connection b/w A and B false =conjoint
c ={4,8}
d={5,6}
c.isdisjoint(d)
True

# superset is independent
# subset is dependent to superset

a={1,2,3,4,5}
b={8,7,6,5,4}
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
a.issubset(b)
False
False
False

a.issuperset(b)
False
a.pop()
1
a
{2, 3, 4, 5}
a.pop()
2
a
{3, 4, 5}
b
{4, 5, 6, 7, 8}
a.pop()
3
a
{4, 5}
b
{4, 5, 6, 7, 8}
a.issubset(b)
True
a.issuperset(b)
False

# dictionary
# ----------

# dictionary is not having index
# dictionary contains ordered collection of data
# dictionary is having(key & value)paired items
# insertion perservation order partially used
# popping also allowed
# no duplicate values

a = {'name':'rk','age':'38','city':'dindigul','degree':'BE'}

type(a)
<class 'dict'>
\
a.keys()
dict_keys(['name', 'age', 'city', 'degree'])
a.value()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
a.values()
dict_values(['rk', '38', 'dindigul', 'BE'])
a.items()
dict_items([('name', 'rk'), ('age', '38'), ('city', 'dindigul'), ('degree', 'BE')])
a['name']
'rk'
a['dindigul']
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a['dindigul']
KeyError: 'dindigul'
a['key']
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a['key']
KeyError: 'key'
a['city']
'dindigul'
# before(:) is called keys and after (:)is called value

>>> 
>>> a.pop('name')
'rk'
>>> a
{'age': '38', 'city': 'dindigul', 'degree': 'BE'}
>>> a.pop('city')
'dindigul'
>>> a.update({'name':'rajesh'})
>>> a
{'age': '38', 'degree': 'BE', 'name': 'rajesh'}
>>> a.update({'name':'kishore'})
>>> a
{'age': '38', 'degree': 'BE', 'name': 'kishore'}
>>> 
...  
>>> # final update will be displayed
>>> 
>>> a.setdefault('gender')
>>> 
>>> a
{'age': '38', 'degree': 'BE', 'name': 'kishore', 'gender': None}
>>> 
>>> a['gender']='male'
>>> a
{'age': '38', 'degree': 'BE', 'name': 'kishore', 'gender': 'male'}
>>> a['name']='kishore'
>>> a
{'age': '38', 'degree': 'BE', 'name': 'kishore', 'gender': 'male'}
