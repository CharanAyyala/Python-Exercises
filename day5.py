#private method usage
class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("From class method, var=",self.__var)
obj=abc(100)
obj._abc__display()


#code to call a class method from another method in the same class
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)
    def add_value(self):
        self.var+=5
        self.display()
obj=abc(10)
obj.add_value()


#class method, which calls a function defind global name space
def aaa(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)
    def modify(self):
        self.var=aaa(self.var)   
obj=abc(10)
obj.display()
obj.modify()
obj.display()


'''builtin functions - get,set,delete
    getattr(),setattr(),delattr()
    hasattr():checks whether the attribute is present or not
'''
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)    
obj=abc(10)
obj.display()
print("Obj has attribute var",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',15)
print("After setting value,var is:",obj.var)
setattr(obj,'count',10)
print("New variable count is created with value",obj.count)
delattr(obj,'var')
print("after deleting",obj.var)


''' builtin class attr
1) .__doc__---when string doc is not specified attr then there will be no return of attr
2) .__dict__---name space accessed attributes
3) .__name__'''
class abc():
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def display(self):
        print("var1:",self.v1)
        print("var2:",self.v2)
obj=abc(10,12.345)
obj.display()
print("object.__dict__:",obj.__dict__)
print("object.__doc__:",obj.__doc__)
print("class.__name__:",abc.__name__)
print("object.__module__:",obj.__module__)
print("class.__bases__:",abc.__bases__)


'''
program that uses class as student to store the name and marks of the student, use a list to store the marks of 3 subjects.
constraints:
1)take class as student
2)create a constructor for the student name
3)create a function for marks,to be entered manually within the class function and add the marks to the list
4)then display student name and the marks he/she got
5)pass the object's attributes of two students names
testcase:
obj1:"vijay"
obj2:"anil"
output:
vijay got [88,88,90]
anil got [87,89,90]
'''
class student():
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("Enter %s marks in %d subject:"%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
obj1=student('vijay')
obj1.entermarks()
obj2=student('anil')
obj2.entermarks()
obj1.display()
obj2.display()


'''program that has a class circle, use a class variable to define the value of constant pi.
use this class variable to calculate the area and circumference of circle with specified radius.
constraints:
pi with the class variable as 3.14159
radius=7.5
return the area and circumference values to main program by creating function with the class respectively 
''' 
class circle():
    pi=3.14159
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.pi*(radius**2)
    def circumference(self):
        return 2*circle.pi*radius
radius=7.5
cir=circle(radius)
area=cir.area()
circumference=cir.circumference()
print(f"Area of circle:{area}")
print(f"Circumference of circle:{circumference}")
