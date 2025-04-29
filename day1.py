#write a program to swap two numbers using circumference symbol
a=1
b=2
a=a^b
b=a^b
a=a^b
print(a,b)

#swap two numbers using conditional applying by logical AND/OR
a=1
b=2
a1=(a|b)&b
b1=(a|b)&a
print(a1,b1)

#swapping using dictionaries
d={'anu':11,'manu':15}
d['anu'],d['manu']=d['manu'],d['anu']
print(d)

#swapping using iter tool
gen=iter([1,2,3])
lst=list(gen)
lst[0],lst[1]=lst[1],lst[0]
print(lst)

#write a program to print the squares of n numbers in a list using single line list comprehension
n=10
print([i*i for i in range(1,11)if i%2!=0])

#strong number
num=int(input("Enter the number:"))
t=num
sum=0
while(num>0):
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
    num//=10
if sum==t:
    print(t,"is strong number")
else:
    print(t,"is not strong number")

#happy number
n=int(input("Enter a number:"))
visit=set()
while n!=1 and n not in visit:
    visit.add(n)
    sum=0
    temp=n
    while temp>0:
        d=temp%10
        sum+=d**2
        temp//=10
    n=sum
if n==1:
    print("Happy")
else:
    print("Not happy")

#nivens number
n=int(input("Enter a number:"))
sum=0
while(n>0):
    rem=n%10    
    sum+=rem
    n//=10
if n%sum==0:
    print("is nivens number")
else:
    print("is not nivens number")    
