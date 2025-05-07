#code for the series 0,0,7,6,14,12...program-1
term=int(input("Enter the term value:"))
value=0
for i in range(1,term+1):
    if i%2==0:
        value=((i//2)-1)*7
    else:
        value=(i//2)*6
print("The",term,"th value is",value)

#program-2
num=int(input("Enter the term value:"))
a,b=0,0
for i in range(1,num+1):
    if i%2!=0:
        a+=7
    else:
        b+=6
if num%2!=0:
    print('{} term of series is {}'.format(num,a-7))
else:
    print('{} term of series is {}'.format(num,b-6))


#for pow of combination of gp series...1,1,2,3,4,9,16,27...
num=int(input("Enter the term value:"))
if num%2==1:
    print(2**(num//2))
else:
    print(3**(num//2-1))


#patterns-- hollow square
n=int(input("Enter number:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


#plus shape
n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==(n//2) or j==(n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


#filled hourglass
n=int(input("Enter the rows:"))
totalrows=2*n-1
for i in range(1,totalrows+1):
    if i<=n:
        spaces=i-1
        stars=2*(n-i)+1
    else:
        spaces=totalrows-i
        stars=2*(i-n)+1
    print(" " * spaces+"*"*stars)


#pascals triangle with binomial coefficient
n=int(input("Enter the rows:"))
for i in range(n):
    print(" " * (n-i),end=' ')
    num=1
    for j in range(i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)
    print()


#loop with list comprehension and empty bucket for pascals triangle
n=int(input("Enter the rows:"))
tri=[[0 for _ in range(i+1)]for i in range(n)]
for i in range(n):
    tri[i][0]=1
    tri[i][i]=1
    for j in range(1,i):
        tri[i][j]=tri[i-1][j-1]+tri[i-1][j]
for i in range(n):
    print(" "*(n-i),end=' ')
    for num in tri[i]:
        print(num,end=' ')
    print()
