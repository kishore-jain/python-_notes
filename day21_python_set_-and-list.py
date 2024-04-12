Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# set

# set is mutable and changeable
# un-ordered and un-indexed
# no duplicate value allowed(77777-7)
# popping of value done from beginning to end
# insertion preservation partially used
# set is basically defind as {}

a={5,3,4,2,1}
a
{1, 2, 3, 4, 5}
name={'arun','mangalyam','muzzi','kishore','jain'}
name
{'arun', 'jain', 'mangalyam', 'muzzi', 'kishore'}

c={23,45,3,6,8,84}
c
{3, 84, 6, 23, 8, 45}
a
{1, 2, 3, 4, 5}
b={8,7,6,5,7,4}
b
{4, 5, 6, 7, 8}
a
{1, 2, 3, 4, 5}
a.add(2)
a
{1, 2, 3, 4, 5}
# beacouse 2 is taken in ouput but duplicate values not allowed.


# list - shallow copy

a=['rk','kayal','alvi','vini']
dup=a
a
['rk', 'kayal', 'alvi', 'vini']
dup
['rk', 'kayal', 'alvi', 'vini']
dup[1]
'kayal'
dup[1]='kanmani'
dup
['rk', 'kanmani', 'alvi', 'vini']
a
['rk', 'kanmani', 'alvi', 'vini']
# shallow copy = change in dupplicate directly affects original structure

a
['rk', 'kanmani', 'alvi', 'vini']


d=a.copy()
a
['rk', 'kanmani', 'alvi', 'vini']
d
['rk', 'kanmani', 'alvi', 'vini']
# a.copy is the correct way to approach the create dupplicate list -it will never distrube the orginal structure.
d[2] = 'sadhana'
d
['rk', 'kanmani', 'sadhana', 'vini']
a
['rk', 'kanmani', 'alvi', 'vini']


# deep copy - change in duplicate will not affect original structure

a
['rk', 'kanmani', 'alvi', 'vini']
a={1,2,3,4,5}

b={4,5,6,7,8}
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
a.difference(b)
{1, 2, 3}
a.difference_update(b)
a
{1, 2, 3}
b
{4, 5, 6, 7, 8}
a.add(4)
a.add(5)
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
a.intersection(b)
{4, 5}
a
{1, 2, 3, 4, 5}
a.intersection(b)
{4, 5}
a.intersection_update(b)
a
{4, 5}
a.add(1)
a.add(2)
a.add(3)
a
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4, 5}
>>> b
{4, 5, 6, 7, 8}
>>> a.discard(8)
>>> a
{1, 2, 3, 4, 5}
>>> a.discard(1)
>>> a
{2, 3, 4, 5}
>>> b
{4, 5, 6, 7, 8}
>>> a.union(b)
{2, 3, 4, 5, 6, 7, 8}
>>> a
{2, 3, 4, 5}
>>> b
{4, 5, 6, 7, 8}
>>> f=[12,34,23,34,23,34]
>>> type(f)
<class 'list'>
>>> f
[12, 34, 23, 34, 23, 34]
>>> f=set(f)
>>> f
{34, 12, 23}
>>> f=list(f)
>>> f
[34, 12, 23]
