# __inti__is used to declare permanent properties to a class
class calci:
    def __init__(self,a,b):
        self.a = a
        self.b = b # instance variable

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def mod (self):
        return self.a % self.b

c = calci(300,50)  # encapsulation # 300 -->a-->self.a  encapsulationmeans  data hiding and dynamic hiding
c1 = calci(25,5)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
print(c1.mod())
# encapsulation cannot be achieved with out using _init_constructor

