#polymorphism
#overloading sample
def hi(name='Henry'):
    print("Hello",name)
hi()
hi('vijay')


#multiple arguments overloading
def abc(*args):
    return sum(args)
print(abc(12,5,35,655))


#simple overloading using class with constructor
class student:
    def __init__(self,name=None,age=None):
        if name and age:
            print(f"Name:{name}, Age:{age}")
        elif name:
            print(f"Name:{name}")
        else:
            print("No data")
student()
student('vijay')
student('steve',25)


'''isinstance()'''
n=99
print(isinstance(n,int))
print(isinstance(n,float))


class pet:
    pass
class dog(pet):
    pass
d=dog()
print(isinstance(d,dog))
print(isinstance(d,pet))


#overloading with operators
class val:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ol):
        return val(self.x+ol.x,self.y+ol.y)
    def __str__(self):
        return f"{self.x},{self.y}"
a=val(1,2)
b=val(3,5)
print(a+b)


'''code for adding two complex numbers, where imaginary numbers and real numbers to be evaluated seperately with 
   __add__() method and raise an error exception with this value where unsupportive data type is encountered
   a=1+2i
   b=3+4i
   output:4+6i
'''
class complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def __add__(self,ol):
        if isinstance(ol,complex):
            return complex(self.r+ol.r,self.i+ol.i)
        else:
            raise TypeError("Unsupported operand-type")
    def __str__(self):
        return f"{self.r}+{self.i}i"
a=complex(1,2)
b=complex(3,4)
print("Result:",a+b)


#overriding redefine the child class which is already exists
class pet:
    def sound(self):
        print("Animal sounds")
class dog(pet):
    def sound(self):
        print("The pet barks!!")
a=pet()
a.sound()
d=dog()
d.sound()


#constructor overriding
class student:
    def __init__(self,name):
        self.name=name
        print("Student constructor")
class person(student):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        print("Person constructor")
s=person('vijay','F')


#method overriding by a polymorphism eval
class pet:
    def sound(self):
        print("Animals sound")
class dog:
    def sound(self):
        print("Barks...")
class cat:
    def sound(self):
        print("Meows...")
pets=[dog(),cat(),pet()]
for p in pets:
    p.sound()


'''code for overriding different parameters in parent method by calculating the area of the circle and square from a parent
   class shape pass side 4 for square and radius 5 for circle.
'''
from math import pi
class shape:
    def area(self):
        return "Area calc is not defined"
class Square(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        return self.s*self.s    
class Circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return pi*(r**2)    
r=int(input("Enter radius:"))
s=int(input("Enter side:"))
square=Square(s)
circle=Circle(r)
print(square.area())
print(circle.area())
