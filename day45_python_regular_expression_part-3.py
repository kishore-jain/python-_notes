Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# regex
# -----

import re

sen ='my fav movie name is NEERPARAVAI & AZHAGI , I have seen these 2 movies for more then 50 times  way back in #2001 and 2013'

len(sen)
121
print(re.findall('\d',sen))
['2', '5', '0', '2', '0', '0', '1', '2', '0', '1', '3']
print(re.findall('\d+',sen))
['2', '50', '2001', '2013']
print(re.findall('\d*',sen))
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '50', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2001', '', '', '', '', '', '2013', '']
print(re.findall('\D',sen))
['m', 'y', ' ', 'f', 'a', 'v', ' ', 'm', 'o', 'v', 'i', 'e', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'N', 'E', 'E', 'R', 'P', 'A', 'R', 'A', 'V', 'A', 'I', ' ', '&', ' ', 'A', 'Z', 'H', 'A', 'G', 'I', ' ', ',', ' ', 'I', ' ', 'h', 'a', 'v', 'e', ' ', 's', 'e', 'e', 'n', ' ', 't', 'h', 'e', 's', 'e', ' ', ' ', 'm', 'o', 'v', 'i', 'e', 's', ' ', 'f', 'o', 'r', ' ', 'm', 'o', 'r', 'e', ' ', 't', 'h', 'e', 'n', ' ', ' ', 't', 'i', 'm', 'e', 's', ' ', ' ', 'w', 'a', 'y', ' ', 'b', 'a', 'c', 'k', ' ', 'i', 'n', ' ', '#', ' ', 'a', 'n', 'd', ' ']
print(re.findall('\D+',sen))
['my fav movie name is NEERPARAVAI & AZHAGI , I have seen these ', ' movies for more then ', ' times  way back in #', ' and ']
print(re.findall('\D*',sen))
['my fav movie name is NEERPARAVAI & AZHAGI , I have seen these ', '', ' movies for more then ', '', '', ' times  way back in #', '', '', '', '', ' and ', '', '', '', '', '']
print(re.findall('\D*',sen))
['my fav movie name is NEERPARAVAI & AZHAGI , I have seen these ', '', ' movies for more then ', '', '', ' times  way back in #', '', '', '', '', ' and ', '', '', '', '', '']
print(re.findall('\w',sen))
['m', 'y', 'f', 'a', 'v', 'm', 'o', 'v', 'i', 'e', 'n', 'a', 'm', 'e', 'i', 's', 'N', 'E', 'E', 'R', 'P', 'A', 'R', 'A', 'V', 'A', 'I', 'A', 'Z', 'H', 'A', 'G', 'I', 'I', 'h', 'a', 'v', 'e', 's', 'e', 'e', 'n', 't', 'h', 'e', 's', 'e', '2', 'm', 'o', 'v', 'i', 'e', 's', 'f', 'o', 'r', 'm', 'o', 'r', 'e', 't', 'h', 'e', 'n', '5', '0', 't', 'i', 'm', 'e', 's', 'w', 'a', 'y', 'b', 'a', 'c', 'k', 'i', 'n', '2', '0', '0', '1', 'a', 'n', 'd', '2', '0', '1', '3']
print(re.findall('\w+',sen))
['my', 'fav', 'movie', 'name', 'is', 'NEERPARAVAI', 'AZHAGI', 'I', 'have', 'seen', 'these', '2', 'movies', 'for', 'more', 'then', '50', 'times', 'way', 'back', 'in', '2001', 'and', '2013']
print(re.findall('\W+',sen))
[' ', ' ', ' ', ' ', ' ', ' & ', ' , ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '  ', ' ', ' ', ' #', ' ', ' ']
print(re.findall('\W',sen))
[' ', ' ', ' ', ' ', ' ', ' ', '&', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ']



# \d -- checks only for digits
# \D -- checks for everything except digits
# \w -- checks for word(alphabe's,numerical value,_)
# \W -- checks for everything except word(only for symbols)
# \s -- checks for whitespaces
# \S -- checks for everything except spaces

# + -- one or more occurence
# --> show continous occurence ex: refer befor example in \w

# * -- 0 or more occurence
# --> show the value where it located

print(re.findall('[A-Z]',sen))
['N', 'E', 'E', 'R', 'P', 'A', 'R', 'A', 'V', 'A', 'I', 'A', 'Z', 'H', 'A', 'G', 'I', 'I']
print(re.findall('[A-Z]+',sen))
['NEERPARAVAI', 'AZHAGI', 'I']
print(re.findall('[A-Z]*',sen))
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'NEERPARAVAI', '', '', '', 'AZHAGI', '', '', '', 'I', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

print(re.findall('[a-z]',sen))
['m', 'y', 'f', 'a', 'v', 'm', 'o', 'v', 'i', 'e', 'n', 'a', 'm', 'e', 'i', 's', 'h', 'a', 'v', 'e', 's', 'e', 'e', 'n', 't', 'h', 'e', 's', 'e', 'm', 'o', 'v', 'i', 'e', 's', 'f', 'o', 'r', 'm', 'o', 'r', 'e', 't', 'h', 'e', 'n', 't', 'i', 'm', 'e', 's', 'w', 'a', 'y', 'b', 'a', 'c', 'k', 'i', 'n', 'a', 'n', 'd']

print(re.findall('[a-z]+',sen))
['my', 'fav', 'movie', 'name', 'is', 'have', 'seen', 'these', 'movies', 'for', 'more', 'then', 'times', 'way', 'back', 'in', 'and']
print(re.findall('[a-z]*',sen))
['my', '', 'fav', '', 'movie', '', 'name', '', 'is', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'have', '', 'seen', '', 'these', '', '', '', 'movies', '', 'for', '', 'more', '', 'then', '', '', '', '', 'times', '', '', 'way', '', 'back', '', 'in', '', '', '', '', '', '', '', 'and', '', '', '', '', '', '']
print(re.findall('[0-9]',sen))
['2', '5', '0', '2', '0', '0', '1', '2', '0', '1', '3']
print(re.findall('\d',sen))
['2', '5', '0', '2', '0', '0', '1', '2', '0', '1', '3']
print(re.findall('^rk','my name is rk'))
[]
print(re.findall('^my','my name is rk'))
['my']
#  ^ -- means starting of s word

print(re.findall('my$','my name is rk'))
[]
print(re.findall('rk$','my name is rk'))
['rk']
#  $ -- mean checking the end of a sentence

print(re.findall('is','my name is rk,my age is 22,my city is vellore'))
['is', 'is', 'is']
print(len(re.findall('is','my name is rk,my age is 22,my city is vellore')))
3
print(re.findall('if_elif_else presention.py','my name is rk,my age is 22,my city is vellore'))
[]
print(re.findall('^my|vellore$','my name is rk,my age is 22,my city is vellore'))
['my', 'vellore']
print(re.findall('^my|vel$','my name is rk,my age is 22,my city is vellore'))
['my']

# to find both starting and ending together

print(re.findall('[vellore]', vellore))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(re.findall('[vellore]', vellore))
NameError: name 'vellore' is not defined
print(re.findall('[vellore]', 'vellore'))
['v', 'e', 'l', 'l', 'o', 'r', 'e']
print(re.findall('[vellore]+', 'vellore'))
['vellore']

sen = '''Anu
Aavi
karan
kavi
kanmani
kinimini
charu
kathir
kasakaasa
eniya
elango
'''

sen
'Anu\nAavi\nkaran\nkavi\nkanmani\nkinimini\ncharu\nkathir\nkasakaasa\neniya\nelango\n'
>>> 
>>> print(re.findall('^rk','my name is rk'))
[]
>>> 
>>> # shortcut for ^-\A
>>> # shortcut for $-\Z
>>> 
>>> print(re.findall('rk\Z','my name is rk'))
['rk']
>>> print(re.findall('\Amy','my name is rk'))
['my']
>>> 
>>> print(re.findall('k',sen))
['k', 'k', 'k', 'k', 'k', 'k', 'k']
>>> print(re.findall('^k',sen))
[]
>>> print(re.findall('k\W',sen))
[]
>>> print(re.findall('k\w',sen))
['ka', 'ka', 'ka', 'ki', 'ka', 'ka', 'ka']
>>> print(re.findall('k\w+',sen))
['karan', 'kavi', 'kanmani', 'kinimini', 'kathir', 'kasakaasa']
>>> print(re.findall('k\w+|k\w+',sen))
['karan', 'kavi', 'kanmani', 'kinimini', 'kathir', 'kasakaasa']
>>> print(re.findall('^k\w+',sen,flags=re.IGNORECASE|re.MULTILINE))
['karan', 'kavi', 'kanmani', 'kinimini', 'kathir', 'kasakaasa']
>>> 
