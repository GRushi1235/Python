#Fibonoci
x=int(0)
y=int(1)
n=input("Enter the length of series: ")
n=int(n)
if n==1:
    print(x)
elif n==2:
    print(x)
    print(y)
else :
    print(x)
    print(y)
while n>2:
    z=x+y
    print(z)
    x=y
    y=z
    n=n-1    
