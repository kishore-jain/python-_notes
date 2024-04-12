Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # inheritance
>>> # -----------
>>> 
>>> # how child cls is accessing the props of a parent cls
>>> 
>>> # sigle inheritance _ if a single child is accessing props of a single parent
>>> 
>>> class RK:
...     def savings(self):
...             print('villa,farm house,car,cast')
... 
...             
>>> class Alvina(RK):
...     '''6 years old girl baby'''
...     pass
... 
>>> a = Alvina()
>>> 
>>> a.saving()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.saving()
AttributeError: 'Alvina' object has no attribute 'saving'. Did you mean: 'savings'?
>>> a.savings()
villa,farm house,car,cast

