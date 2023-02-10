a=int(input("Enter the number to find fact:  "))

def fact(n):
    if (n==1 or n==0) :
        return 1
    else :
        return (int(n) * fact(int(n) - 1))
    
print("fact of ",a,"is ",fact(a) )    