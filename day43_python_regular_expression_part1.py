Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # regular expression
>>> # ------------------
>>> 
>>> # it's a technique used to check whether the given pattern is available inside a searching sentence
>>> 
>>> # in a simple terms, regex means PATTEREN MATCHING concept
>>> 
>>> # in java - we have a pattern class to get pattern value, matcher class to match the pattern with a sentence
>>> 
>>> # in example :
>>> 
>>> # ==> pattern means
>>> 
>>> # pattern ==> find a in rajesh kumar
>>> # sentence ==> my name is rajesh kumar alias rk
>>> 
>>> # here, a is pattern and remaining is sentence
>>> 
>>> # in python , import regex module to achieve pattern matching
>>> 
>>> # realtime benfits
>>> # ----------------
>>> 
>>> # find and findall / replace and replaceall
>>> # page validation / login page authentication
>>> # email processing
>>> # face recognition / finger print / goggle lens
>>> # mobile pattern lock / checking phone contacts / apps checkup
>>> # adoptive brightness
>>> # sensor based valet parking / secured home / pos machine
>>> # wifi / wifi enabled atm cards / fastag - tollgate services
>>> # hostpost / telegram / gmaps / google earth
# raining maps / qr code / digital image processing / phone image editiors

# regex stages :
# --------------

# pattern creation - [ signup process - user registration ] also said to be pattern composition
# pattern matching [ checks the length of characters entered username, password ]
# pattern recongnition [ checks for mandatory fields in password like upper, lower, numbers and symbols ]
# pattern repetition [ checks character by character ]
# pattern transformation [ qrcode, face recognition, nearby search ]
# pattern transition [ otp code / barcode / marse code / ifsc code / image based captcha / i am robot / moving login ]
# pattern decomposition [ access granted after session close ]

# regex operations
# ----------------

# match()
# search()
# findall()
# split()
# sub()
# compile()

# to import regex use import re

import re

pat = 'rk'

sen = 'my name is rajeshkumar alias rk'

print(re.Match(pat, sen))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(re.Match(pat, sen))
TypeError: cannot create 're.Match' instances

print(re.match(pat, sen))
None

# match() --> it checks for the patterns availability only at the very beginning of the sentence

sen1 = 'rk is my name'
print(re.match(pat, sen))
None

print(re.match(pat, sen1))
<re.Match object; span=(0, 2), match='rk'>

# span show index where rk is ..


# search ()

# --> it checks for pattern availability anywhere inside the sentence

sen
'my name is rajeshkumar alias rk'
pat
'rk'

print(re.match(pat, sen))
None
print(re.search(pat, sen))
<re.Match object; span=(29, 31), match='rk'>

print(re.search('dk', sen))
None

print(re.search('a', sen))
<re.Match object; span=(4, 5), match='a'>

# findall() - it checks for the multiple occurence of a pattern value

print(re.findall('a', sen))
['a', 'a', 'a', 'a', 'a']

print(len(re.findall('a', sen)))
5

# split
print(re.split('a', sen))
['my n', 'me is r', 'jeshkum', 'r ', 'li', 's rk']
sen
'my name is rajeshkumar alias rk'

# sub - replaces a character with another character

print(re.sub('a','A', sen))
my nAme is rAjeshkumAr AliAs rk

sen
'my name is rajeshkumar alias rk'
