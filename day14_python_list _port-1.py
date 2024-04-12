Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# python native datatype [non primitive-built in type]

# list []
# tuple ()
# set {values}
# dictionary {key:value}

# list
# ----

# properties of list
# ------------------

# list of ordered collection of data items
# list value are indexed
# list supports duplicate values
# list follow insertion preservation order
# list allow popping of value from end to beginning
# list follow LIFO
# LIST supports hetrogenous values
# notes: LIFO = last in first out


fruit = ['orange','mango','apple','grapes','papaya','guava']

type(fruit)
<class 'list'>
fruit
['orange', 'mango', 'apple', 'grapes', 'papaya', 'guava']
fruit[0]
'orange'
fruit[1]
'mango'
fruit[2]
'apple'
fruit[3]
'grapes'
fruit[4]
'papaya'
fruit[5]
'guava'
fruit[-1]
'guava'
fruit[-2]
'papaya'
fruit[-3]
'grapes'
fruit[1:4]
['mango', 'apple', 'grapes']
fruit
['orange', 'mango', 'apple', 'grapes', 'papaya', 'guava']
fruit[0]='apple'
fruit
['apple', 'mango', 'apple', 'grapes', 'papaya', 'guava']
k
# poping: last in first out

fruit.pop()
'guava'
fruit.[::-1]
SyntaxError: invalid syntax
fruit.(::-1)
SyntaxError: invalid syntax

fruit.pop(1)
'mango'
fruit
['apple', 'apple', 'grapes', 'papaya']
# pop remove the value permenantly

fruit[::-1]
['papaya', 'grapes', 'apple', 'apple']


# list supporting functions
# -------------------------

fruit
['apple', 'apple', 'grapes', 'papaya']

fruit.append('rk')

fruit
['apple', 'apple', 'grapes', 'papaya', 'rk']

# append alwayes add value at end
# only one value should be added at the time

fruit.clear()

fruit
[]

fruit.append('kivi')

fruit
['kivi']

fruit.append('black_current')

fruit
['kivi', 'black_current']

fruit.extend(['mango','guava','grapes','amla'])
fruit
['kivi', 'black_current', 'mango', 'guava', 'grapes', 'amla']

# []should be used in extend list is passed in another list.

fruit.append('kivi')

fruit
['kivi', 'black_current', 'mango', 'guava', 'grapes', 'amla', 'kivi']

fruit.count('kivi')
2

fruit.count('')
0

fruit.index('kivi')
0
fruit[2]='kivi'

fruit
['kivi', 'black_current', 'kivi', 'guava', 'grapes', 'amla', 'kivi']

fruit[o]==fruit[2]
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    fruit[o]==fruit[2]
NameError: name 'o' is not defined
fruit[2]==fruit[0]
True
fruit[2]==fruit[0]==fruit[6]
True
fruit.insert(2,'rk')

fruit
['kivi', 'black_current', 'rk', 'kivi', 'guava', 'grapes', 'amla', 'kivi']

fruit.remove('black_current')

fruit
['kivi', 'rk', 'kivi', 'guava', 'grapes', 'amla', 'kivi']
fruit.remove('kivi')

fruit
['rk', 'kivi', 'guava', 'grapes', 'amla', 'kivi']

fruit.pop(1)
'kivi'

fruit
['rk', 'guava', 'grapes', 'amla', 'kivi']

fruit.reverse()
'
fruit
['kivi', 'amla', 'grapes', 'guava', 'rk']

fruit[::-1]
['rk', 'guava', 'grapes', 'amla', 'kivi']

fruit
['kivi', 'amla', 'grapes', 'guava', 'rk']

fruit.sort()

fruit
['amla', 'grapes', 'guava', 'kivi', 'rk']
>>> 
>>> # sort the list in aplabet order
>>> 
>>> fruit.append(90)
>>> fruit
['amla', 'grapes', 'guava', 'kivi', 'rk', 90]
>>> 
>>> fruit.sort()
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    fruit.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> fruit.pop()
90
>>> 
>>> fruit
['amla', 'grapes', 'guava', 'kivi', 'rk']
>>> # -------------------------------------------------------------------------------------------------------------------
>>> 
>>> # task
>>> 
>>> # bick -> pulser, apache, r15, ninja, meteor, mt15,interceptor
>>> 
>>> # index wise display
>>> # checking duplicate
>>> # count of duplivate
>>> # sorting of value
>>> # reverse list
>>> # create list
'''''''''''''''''''
