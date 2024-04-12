Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# user defined functions
# ----------------------

# customised functions/explicit functions

# Rules
# -----

# use def keyword at the beginning
# provide a meaningful function name name followed by () and :
# declare body statements
# call the function to get the output

def biodata():
    name='gk'
    age=21
    city='thiruvallu'
    hobby='playing'
    print(name,age,city,hobby)

    

biodata
<function biodata at 0x0000015C4FB679A0>
biodata()
gk 21 thiruvallu playing
# it is an function call()
biodata()
gk 21 thiruvallu playing
biodata()
gk 21 thiruvallu playing
biodata()
gk 21 thiruvallu playing

# this is the example for function with no parmater

# function with  parameters
# -------------------------

def carinfo(carbrand, carmodel, carprice):
    print('my fav car brand is ',carbrand)
    print('my fav car model is ',carmodel)
    print('my fav car proce is ',catprice)

    
carinfo('skoda','yeti',1340000)
my fav car brand is  skoda
my fav car model is  yeti
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    carinfo('skoda','yeti',1340000)
  File "<pyshell#38>", line 4, in carinfo
    print('my fav car proce is ',catprice)
NameError: name 'catprice' is not defined. Did you mean: 'carprice'?
def carinfo(carbrand, carmodel, carprice):
    print('my fav car brand is ',carbrand)
    print('my fav car model is ',carmodel)
    print('my fav car proce is ',carprice)

    
carinfo('skoda','yeti',1340000)
my fav car brand is  skoda
my fav car model is  yeti
my fav car proce is  1340000
carinfo(1340000,'skoda','yeti')
my fav car brand is  1340000
my fav car model is  skoda
my fav car proce is  yeti
carinfo('hyundai','santafe',1750000)
my fav car brand is  hyundai
my fav car model is  santafe
my fav car proce is  1750000
carinfo('toyota','supra',1750000)
my fav car brand is  toyota
my fav car model is  supra
my fav car proce is  1750000
# this is example for reusable code templete

# the content given while in output called arguments

# Type of arguments in user defined function
# ------------------------------------------

# default arguments
# positional arguments
# keyword arguments

# variable length arguments

# default arguments
# -----------------

def bikeinfo(brand='bajaj',model='platina',price=85000):
    print('bike brand name is ',brand)
    print('bike model name is ',model)
    print('bike price is ',price)

    
bikeinfo()
bike brand name is  bajaj
bike model name is  platina
bike price is  85000

bikeinfo('yamaha','r15',200000)
bike brand name is  yamaha
bike model name is  r15
bike price is  200000
>>> 
>>> # if not any arguments in while function is calling it takes by default value given while declearing
>>> 
>>> bikeinfo('hero','splender')
bike brand name is  hero
bike model name is  splender
bike price is  85000
>>> # it take the lest  value by default
>>> 
>>> # keyword arguments
>>> # ------------------
>>> 
>>> bikeinfo(model='pulser',price=200000)
bike brand name is  bajaj
bike model name is  pulser
bike price is  200000
>>> # another name for parameter is keyword
>>> 
>>> bikeinfo()
bike brand name is  bajaj
bike model name is  platina
bike price is  85000
>>> # can change particular parameter only keyword argument is used
>>> 
>>> 
