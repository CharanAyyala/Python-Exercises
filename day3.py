#basic function
def hi(name):
    return f"Hello,{name}!"
print(hi("Students"))

#default parameters
def a(x,y=1):
    return x*y
print(a(5))
print(a(5,3))

#with variable arguments creates an empty bucket to hold arguments
def sn(*args):
    return sum(args)
print(sn(1,2,3))
print(sn(10,20,30,40))

#function with keyword args
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
info(name='mana',age=15,city='mumbai')

#lambda fun
sq=lambda a:a*a
print(sq(4))
add=lambda x,y:x+y
print(add(5,9))

#write a program to return multiple values min,max,avg by passing 1,2,3,4,5 to a function
def mul_values(*args):
    return f"Min:{min(args)},Max:{max(args)},Avg:{sum(args)/len(args)}"
print(mul_values(1,2,3,4,5))

#recursive functions---fact(direct recursion)
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

#recursive functions---fact(indirect)
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
print(is_even(4))
print(is_odd(7))

'''create a program to determine if a string is a palindrome by recursively comparing characters from start to end by base
case function and call if the pointer meets it's palindrome constraints
    constraints:
    def is_palindrome length
    def check_palindrome start,end,string(s)
    input:
    racecar=True
    hello=False
    level=True
'''
def is_p(s):
    if len(s)<=1:
        return True
    return check_p(s,0,len(s)-1)
def check_p(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    return is_p(s[start+1:end])
print(is_p("racecar"))
print(is_p("hello"))
print(is_p("level"))

#tail recursion using accumulator(acc)
def ftail(n,acc=1):
    if n==0 or n==1:
        return acc
    return ftail(n-1,n*acc)
print(ftail(5))

#nested function
def fun(n):
    if n>50:
        return n-5
    else:
        return fun(fun(n+5)+3)
print(fun(40))

#super factorial
def sfact(n):
    if n<=0:
        return 1
    return fact(n)*sfact(n-1)
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print(sfact(4))

#power tower-nested recursion
def pt(a,n):#(base,exponent)
    if n==1:
        return a
    return a**pt(a,n-1)  
print(pt(4,2))
print(pt(3,2))
