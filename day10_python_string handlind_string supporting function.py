Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name='sri kanth'
name.isalnum()
False
name.isalpha()
False

name.isascii()
True
name.isdecimal()
False
name.isdigit()
False
name.isidentifier()
False
name
'sri kanth'
name='sri_kanth'
name.isidentifier()
True

name.isalpha()
False

name='python programming'
name.islower()
True

name.isnumeric()
False

name.isprintable()
True

name='python programming'

name.islower()
True

name.isspace()
False
name.' '
SyntaxError: invalid syntax
name=' '
name.isspace()
True

name='python programming'
name.istitle()
False

name.title()
'Python Programming'
name.isupper
<built-in method isupper of str object at 0x000001827AA31660>
name.isupper()
False

name.upper()
'PYTHON PROGRAMMING'
name.jion()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    name.jion()
AttributeError: 'str' object has no attribute 'jion'
'#'.jion(name)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    '#'.jion(name)
AttributeError: 'str' object has no attribute 'jion'
'#'.join(name)
'p#y#t#h#o#n# #p#r#o#g#r#a#m#m#i#n#g'

name.join('#')
'#'
name
'python programming'

'#'.join('rk','alvi')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    '#'.join('rk','alvi')
TypeError: str.join() takes exactly one argument (2 given)
a=('rk','alvi')
'#'.join(a)
'rk#alvi'

name.partition('')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    name.partition('')
ValueError: empty separator

name.partition(' ')
('python', ' ', 'programming')

name.partition('g')
('python pro', 'g', 'ramming')

name.replace('p','P')
'Python Programming'

name.replace('r','R')
'python pRogRamming'

name.find('r')
8
name
'python programming'
name.rfind
<built-in method rfind of str object at 0x000001827AA31660>
name.rfind()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    name.rfind()
TypeError: rfind() takes at least 1 argument (0 given)
name.rfind('r')
11
name.rindex('p')
7
name.index('p')
0
name.index('n')
5
name.rindex('n')
16
name[-2]
'n'
name[-2]==name[16]
True

name.split(' ')
['python', 'programming']
name.split('p')
['', 'ython ', 'rogramming']
name.split('o')
['pyth', 'n pr', 'gramming']
name.split()
['python', 'programming']
name.staryswith('p')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    name.staryswith('p')
AttributeError: 'str' object has no attribute 'staryswith'. Did you mean: 'startswith'?
>>> name.startswith('p')
True
>>> name='alvina'
>>> name.swapcase()
'ALVINA'
>>> name.swapcase()
'ALVINA'
>>> name.strip()
'alvina'
>>> # strip mean raping
>>> 
>>> # strip always work with corner
>>> 
>>> name.strip('a')
'lvin'
>>> name.lstrip('a')
'lvina'
>>> name.rstrip('a')
'alvin'
>>> name.lstrip('v')
'alvina'
>>> 'kavin'.strip('k')
'avin'
>>> 
>>> 
>>> #Task:
>>> # download a pagagraph from the net count the number of words in paragraph
>>> # print the top 3 words.
>>> # most repeatedly used word(top 3 words)
>>> # count of the 3 frequently used words
