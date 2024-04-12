Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User defined functions
#-----------------------

#customised functions / explicit functions

#Rules:
#-------

# 1. Use Def keyword at the beginning
# 2. provide a meaningful function name
#2. follwoed by () and :
# 3. Declare body statements
# 4. call the function to get the output.

def biodata():
    name='rk'
    age=38
    city='dindigul'
    hobby='singing'
    print(name,age,city,hobby)

    
biodata
<function biodata at 0x000002D14EBF79A0>
biodata()
rk 38 dindigul singing

biodata()
rk 38 dindigul singing

#this is the example for function with no parameters

def bio(4,3):
    
SyntaxError: invalid syntax
import math
def bio(4,3)
SyntaxError: invalid syntax


#function with parameters
#-------------------------

def carinfo(carbrand, carmodel,carprice):
    print('my fav car brand is', carbrand)
    print('my fav car model is', carmodel)
    print('my fav car price is', carprice)

    
carinfo('skoda','yeti',1350000)
my fav car brand is skoda
my fav car model is yeti
my fav car price is 1350000

carinfo(1350000,'skoda','yeti')
my fav car brand is 1350000
my fav car model is skoda
my fav car price is yeti

carinfo('lamborghini','hurricane','4Cr')
my fav car brand is lamborghini
my fav car model is hurricane
my fav car price is 4Cr

carinfo('toyota','supra',7800000)
my fav car brand is toyota
my fav car model is supra
my fav car price is 7800000

# Types of arguments in user defined function
#--------------------------------------------

# default arguments
# positional arguments
# keyword arguments

# variable length arguments


#Default Arguments
O#-----------------

def bikeinfo(brand, model, price)
SyntaxError: incomplete input
... def bikeinfo(brand='bajaj', model='platina', price=95000):
...     print('bike brand name is', brand)
...     print('bike model name is', model)
...     print('bike price is', price)
... 
...     
... bikeinfo()
... bike brand name is bajaj
... bike model name is platina
... bike price is 95000
... 
... bikeinfo('herio','splendor',90000)
... bike brand name is herio
... bike model name is splendor
... bike price is 90000
... 
... bikeinfo('hero', 'splendor')
... bike brand name is hero
... bike model name is splendor
... bike price is 95000
... 
... #keyword argument
... #----------------
... 
... bikeinfo(model='pulsar',price=150000)
... bike brand name is bajaj
... bike model name is pulsar
... bike price is 150000
