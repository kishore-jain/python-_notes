Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Quantifiers in regex
>>> # --------------------
>>> 
>>> # ? - once or not
>>> # + - once or more
>>> # * - zero or more
>>> 
>>> # meta - character and meta tag
>>> # -----------------------------
>>> 
>>> # //d - digits 0-9
>>> #  --> worngly written
>>> 
>>> 
>>> # \d - digits 0-9
>>> # \D - except digits (non digits)
>>> # \w - alpha numeric word (a-z, A-Z, 0-9, _ )
>>> # \W - except alpha numeric word (only symbols)
>>> # \s - white spaces
>>> # \S - except white spaces
>>> # [abc] - either a or b or c
>>> # [^abc] -except either a or b or c
>>> # [0-9]{6} - only numbers, only six digits numbers
>>> # [0-9]{6,} - only numbers, only six digits numbers or more
>>> # [0-9]{6,10} - only numbers, min 6 but less than 10
>>> 
>>> # outside the square barckets ^ and $ - means the word should start with that word and ends with that word
>>> # Example -> "^dk$" , "Deepak"
>>> 
>>> import re
>>> 
>>> sen = 'My name is rajeshkumar @ rk, i am from dindigul # Briyani city, aged 38 years born on 25 sep 1985, mail id iaamrk@gmail.com, password is muzhi@2033'

len(sen)
147

print(re.search('\d',sen))
<re.Match object; span=(69, 70), match='3'>

print(re.findall('\d',sen))
['3', '8', '2', '5', '1', '9', '8', '5', '2', '0', '3', '3']

print(re.findall('\d+',sen))
['38', '25', '1985', '2033']

print(re.findall('\d*',sen))
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '38', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '25', '', '', '', '', '', '1985', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2033', '']


print(re.findall('\D',sen))
['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'r', 'a', 'j', 'e', 's', 'h', 'k', 'u', 'm', 'a', 'r', ' ', '@', ' ', 'r', 'k', ',', ' ', 'i', ' ', 'a', 'm', ' ', 'f', 'r', 'o', 'm', ' ', 'd', 'i', 'n', 'd', 'i', 'g', 'u', 'l', ' ', '#', ' ', 'B', 'r', 'i', 'y', 'a', 'n', 'i', ' ', 'c', 'i', 't', 'y', ',', ' ', 'a', 'g', 'e', 'd', ' ', ' ', 'y', 'e', 'a', 'r', 's', ' ', 'b', 'o', 'r', 'n', ' ', 'o', 'n', ' ', ' ', 's', 'e', 'p', ' ', ',', ' ', 'm', 'a', 'i', 'l', ' ', 'i', 'd', ' ', 'i', 'a', 'a', 'm', 'r', 'k', '@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm', ',', ' ', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd', ' ', 'i', 's', ' ', 'm', 'u', 'z', 'h', 'i', '@']
print(re.findall('\D+',sen))
['My name is rajeshkumar @ rk, i am from dindigul # Briyani city, aged ', ' years born on ', ' sep ', ', mail id iaamrk@gmail.com, password is muzhi@']

print(re.findall('\D*',sen))
['My name is rajeshkumar @ rk, i am from dindigul # Briyani city, aged ', '', '', ' years born on ', '', '', ' sep ', '', '', '', '', ', mail id iaamrk@gmail.com, password is muzhi@', '', '', '', '', '']


print(re.findall('\w',sen))
['M', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'r', 'a', 'j', 'e', 's', 'h', 'k', 'u', 'm', 'a', 'r', 'r', 'k', 'i', 'a', 'm', 'f', 'r', 'o', 'm', 'd', 'i', 'n', 'd', 'i', 'g', 'u', 'l', 'B', 'r', 'i', 'y', 'a', 'n', 'i', 'c', 'i', 't', 'y', 'a', 'g', 'e', 'd', '3', '8', 'y', 'e', 'a', 'r', 's', 'b', 'o', 'r', 'n', 'o', 'n', '2', '5', 's', 'e', 'p', '1', '9', '8', '5', 'm', 'a', 'i', 'l', 'i', 'd', 'i', 'a', 'a', 'm', 'r', 'k', 'g', 'm', 'a', 'i', 'l', 'c', 'o', 'm', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd', 'i', 's', 'm', 'u', 'z', 'h', 'i', '2', '0', '3', '3']

print(re.findall('\w+',sen))
['My', 'name', 'is', 'rajeshkumar', 'rk', 'i', 'am', 'from', 'dindigul', 'Briyani', 'city', 'aged', '38', 'years', 'born', 'on', '25', 'sep', '1985', 'mail', 'id', 'iaamrk', 'gmail', 'com', 'password', 'is', 'muzhi', '2033']

print(re.findall('\w*',sen))
['My', '', 'name', '', 'is', '', 'rajeshkumar', '', '', '', 'rk', '', '', 'i', '', 'am', '', 'from', '', 'dindigul', '', '', '', 'Briyani', '', 'city', '', '', 'aged', '', '38', '', 'years', '', 'born', '', 'on', '', '25', '', 'sep', '', '1985', '', '', 'mail', '', 'id', '', 'iaamrk', '', 'gmail', '', 'com', '', '', 'password', '', 'is', '', 'muzhi', '', '2033', '']

print(re.findall('\W',sen))
[' ', ' ', ' ', ' ', '@', ' ', ',', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', '@', '.', ',', ' ', ' ', ' ', '@']

print(re.findall('[a-z]',sen))
['y', 'n', 'a', 'm', 'e', 'i', 's', 'r', 'a', 'j', 'e', 's', 'h', 'k', 'u', 'm', 'a', 'r', 'r', 'k', 'i', 'a', 'm', 'f', 'r', 'o', 'm', 'd', 'i', 'n', 'd', 'i', 'g', 'u', 'l', 'r', 'i', 'y', 'a', 'n', 'i', 'c', 'i', 't', 'y', 'a', 'g', 'e', 'd', 'y', 'e', 'a', 'r', 's', 'b', 'o', 'r', 'n', 'o', 'n', 's', 'e', 'p', 'm', 'a', 'i', 'l', 'i', 'd', 'i', 'a', 'a', 'm', 'r', 'k', 'g', 'm', 'a', 'i', 'l', 'c', 'o', 'm', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd', 'i', 's', 'm', 'u', 'z', 'h', 'i']

print(re.findall('[a-z]+',sen))
['y', 'name', 'is', 'rajeshkumar', 'rk', 'i', 'am', 'from', 'dindigul', 'riyani', 'city', 'aged', 'years', 'born', 'on', 'sep', 'mail', 'id', 'iaamrk', 'gmail', 'com', 'password', 'is', 'muzhi']

print(re.findall('[A-Z]+',sen))
['M', 'B']
print(re.findall('[A-Z]*',sen))
['M', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'B', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

