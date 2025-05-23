'''errors and exceptions
   types of errors or exceptions
   try-block
   except
   finally
   raising exception
   built-in functions
'''


#zero division error
5/0


#name error
v+10


#type error
'vijay'+222


#handling zero division error
num=int(input("Enter the numerator:"))
deno=int(input("Enter the denominator:"))
try:
    quo=num/deno
    print("Quotient:",quo)
except ZeroDivisionError:
    print("Denominator cannot be zero")


#multiple exception handling
try:
    num=int(input("Enter number:"))
    print(n**2)
except KeyboardInterrupt:
    print("You have to enter a number...not string")
except ValueError:
    print("Please check before you enter...program end")
print("Byee")


#multiple exception in a single block handling
try:
    n=int(input("Enter number:"))
    print(n**2)
except (KeyboardInterrupt,ValueError,TypeError):
    print("Please check before you enter...program end")
print("Byee")


#raise an exception
try:
    num=4
    print(num)
    raise ValueError
except:
    print("""even executing perfectly...exception raise manually""")


#re-raise an error
try:
    raise NameError
except:
    print("re-raise")
    raise


#instance using in exceptions
try:
    raise Exception('hi','students')
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    print(errorObj)
    x,y=errorObj.args
    print("Assigned1:",x)
    print("Assigned2:",y)


#handling in functions
def div(n,d):
    try:
        q=n/d
        print(q)
    except ZeroDivisionError:
        print("non-processed")
a=int(input("Enter numerator:"))
b=int(input("Enter denominator:"))
div(a,b)


class myError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
try:
    raise myError(99)
except myError as e:
    print("Returned string is:",e.value)
    print(type(e.value))
    

try:
    print('raise exception')
    raise ValueError
finally:
    print("performing cleanup by finally")


try:
    print("abc")#raise exception
    raise ValueError
except:
    print('123')#recive exception
finally:
    print('abc123')#ignore process


#interactive calc model with python operation
'''using class exceptions modules'''
class Calculator:
    def __init__(self):
        self.one=0
        self.two=0
    def input_numbers(self):
        try:
            self.one=float(input("Enter 1st number:"))
            self.two=float(input("Enter 2nd number:"))
        except ValueError:
            print("Invalid input....please enter numbers")
            self.input_numbers()
    def add(self):
        return self.one+self.two
    def subtract(self):
        return self.one-self.two
    def multiply(self):
        return self.one*self.two
    def divide(self):
        if self.two==0:
            raise ZeroDivisionError("cannot divide with zero")
        return self.one/self.two
    def modulo(self):
        return self.one%self.two
    def expo(self):
        return self.one**self.two
    def floor_divide(self):
        return self.one//self.two
def display_menu():
    print("\n ==== CALCULATOR MENU ==== \n")
    print("1. Addition(+)")
    print("2. Subtract(-)")
    print("3. Multiply(*)")
    print("4. Divide(/)")
    print("5. Modulo(%)")
    print("6. Expo(**)")
    print("7. Floor Division(//)")
    print("8. Exit")
def main():
    calc=Calculator()
    while True:
        display_menu()
        choice=input("select an operation (1-8):")
        if choice=='8':
            print("Exit")
            break
        calc.input_numbers()
        try:
            if choice=='1':
                print("Result:",calc.add())
            elif choice=='2':
                print("Result:",calc.subtract())
            elif choice=='3':
                print("Result:",calc.multiply())
            elif choice=='4':
                print("Result:",calc.divide())
            elif choice=='5':
                print("Result:",calc.modulo())
            elif choice=='6':
                print("Result:",calc.expo())
            elif choice=='7':
                print("Result:",calc.floor_divide())
            else:
                print("Invalid choice,select from 1-8")
        except ZeroDivisionError as e:
            print("Error:",e)
        except Exception as e:
            print("Unexpected error",e)
main()
