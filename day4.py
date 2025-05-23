#basic oops concept of python
class abc():
    var=100
    def display(self):
        print("This is class method")
obj=abc()
print(obj.var)
obj.display()


#class constructor __init__(method)
class abc():
    def __init__(self,val):
        print("This is a class method")
        self.val=val
        print("The value is:",val)
obj=abc(10)


#class variable-cv, object variable-ov
class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("Object var:",var)
        print("Class var:",abc.cv)
obj=abc(10)
obj=abc(20)
obj=abc(30)


'''code to illustrate the modifications of an instance variable to check whether the passing attribute is even or odd,
by creating a class number and function to check even or odd'''
class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def eo(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.eo(23)


'''segregate the even and odd parameters in a list and print even list and odd list sepeartely using a class "number"
    n1=number(21)
    n2=number(32)
    n3=number(43)
    n4=number(54)
    n5=number(65)
    output:even numbers:[32,54]
           odd numbers:[21,43,65]
'''
class number():
    even=[]
    odd=[]
    def __init__(self,val):
        self.val=val
        if val%2==0:
            number.even.append(val)
        else:
            number.odd.append(val)
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("Even numbers:",number.even)
print("Odd numbers:",number.odd)


#delete method- __del__()
class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("Object var:",var)
        print("Class var:",abc.cv)
    def __del__(self):
        abc.cv-=1
        print("Object with %d is going out of scope "%self.var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)
del obj1
del obj2
del obj3


'''
__repr__ ---> returns string representation 
__cmp__ ---> compares two class objects
__len__ ---> length of object
'''
class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj=abc("abcdef",10)
print("The value stored in object is:",repr(obj))
print("The length of name stored in object:",len(obj))
obj1=abc("ghijkl",1)
val=obj.__cmp__(obj1)
if val==0:
    print("Both the values are equal")
elif val==-1:
    print("First value is less than second")
else:
    print("Second value is less than first")


# __getitem__(), __setitem__() methods
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist)
numlist[3]=10
print(numlist.mylist)
