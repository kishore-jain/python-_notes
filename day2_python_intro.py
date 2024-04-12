Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# pythons tokens / python language components

#-------------------------------------------------

# 1.identifiers
# 2.literals
# 3.operators
# 4.keywords
# 5.comments
# 6.quotations


# 1. identifier
# ---------------

# identifier means named memory reference location/locators

# identifier in python means variables or value containers

 name='alvina rk'
 
SyntaxError: unexpected indent
age=6
gender = 'female'

#  here name,age,city is called identifiers

 id(name)
 
SyntaxError: unexpected indent
id(name)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    id(name)
NameError: name 'name' is not defined
id(name)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    id(name)
NameError: name 'name' is not defined
id(age)
2806612623760
id(gender)
2806653990704
id(name)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    id(name)
NameError: name 'name' is not defined







id(rajesh)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    id(rajesh)
NameError: name 'rajesh' is not defined
name='alvina rk'
id(name)
2806654068656

id(rajesh)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    id(rajesh)
NameError: name 'rajesh' is not defined
id('rajesh')
2806654064496
>>> 'rajesh'
'rajesh'
>>> # rules
>>> #---------
>>> 
>>> # identifiers cannot start with number
>>> # identifiers cannot be a keyword
>>> # identifiers cannot be a builtin function
>>> # identifiers may start with alphabets
>>> # identifiers may also start with underscore
>>> 
>>> # types
>>> #-------
>>> 
>>> # private identifier
>>> # strong private identifier
>>> # magical method identifier(starts with_and ends with_)
>>> 
>>> _name='elango'
>>> 
>>> _11ambatch_name='elongo'
>>> rk_11ambatch_name='elango'
>>> 
>>> # private identifier-name=elango
>>> # strong private identifier-name='elango'
>>> # magical method identifier-name='elango'
>>>  Today call
...  
SyntaxError: unexpected indent
