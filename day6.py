#multiple inhertance
class base1(object):   #1st base-class
    def __init__(self):
        super(base1,self).__init__()
        print("Base Class-1")
class base2(object):     #2nd base-class
    def __init__(self):
        super(base2,self).__init__()
        print("Base Class-2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("Derived class from both classes")
d=derived()


'''initialise classes addition,multiplication in a calculator, pass the values from main program to the superclass,
   where the subclasses addition and multiplication were triggered and return the outputs respectively
   1) take derived class cal
   2)from derived class call subclasses add and mul
   3)return the values after math to the object
   4)manual values of both numbers considered within the object
'''
class addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Addition is also initialised")
    def add(self):
        return self.a+self.b
class multiplication:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Multiplication is also initialised")
    def mul(self):
        return self.a*self.b
class calc(addition,multiplication):
    def __init__(self,a,b):
        addition.__init__(self,a,b)
        multiplication.__init__(self,a,b)
        print("Class calc initialized")
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=calc(a,b)
print("Sum:",c.add())
print("Product:",c.mul())


'''tnitialise classes square,cube  in a class, pass the values from main program to the superclass,
   where the subclasses square and cube are triggered and return the outputs respectively
   1) take derived class 
   2)from derived class call subclasses sq and cb
   3)return the values after math to the object
   4)add the values of sq and cb and return the added value
'''
class square:
    def __init__(self,a):
        self.a=a
        print("Square initialised")
    def sq(self):
        return self.a**2
class cube:
    def __init__(self,a):
        self.a=a
        print("Cube initialised")
    def cb(self):
        return self.a**3
class num(square,cube):
    def __init__(self,a):
        square.__init__(self,a)
        cube.__init__(self,a)
        print("Class num initialised")
a=int(input("Enter a value:"))
b=num(a)
print("Square:",b.sq())
print("Cube:",b.cb())
print("Sum of sq and cb is:",b.sq()+b.cb())


#multi level inheritance
class person:  #base class
    def name(self):
        print("Name......")
class teacher(person):   #derived class
    def qualification(self):
        print("Phd")
class hod(teacher):
    def exp(self):
        print("Experience....15yrs")
head=hod()
head.name()
head.qualification()
head.exp()


#multi level inheritance cubes and squares of an obj
class num:
    def __init__(self,n):
        self.n=n
        print("Number initialized")
class sq(num):
    def square(self):
        return self.n**2
class cu(sq):
    def cube(self):
        return self.n**3
calc=cu(int(input("Enter num:")))
print("square:",calc.square())
print("Cube:",calc.cube())


#hierarchy inheritance
class number:
    def __init__(self,num):
        self.num=num
    def get_number(self):
        return self.num
class double(number):
    def result(self):
        return self.get_number()*2
class triple(number):
    def result(self):
        return self.get_number()*3
d=double(int(input("Enter value:")))
print("Double:",d.result())
t=triple(int(input("Enter value:")))
print("Triple:",t.result())


#abstract class
class fruit:
    def taste(self):
        raise NotImplementedError()
    def vitamin(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "Sweet"
    def vitamin(self):
        return "Vitamin-A"
    def color(self):
        return "Yellow"
class orange(fruit):
    def taste(self):
        return "Sour&Sweet"
    def vitamin(self):
        return "Vitamin-C"
    def color(self):
        return "orange"
alphanso=mango()
print(alphanso.taste(),alphanso.vitamin(),alphanso.color())
org=orange()
print(org.taste(),org.vitamin(),org.color())


