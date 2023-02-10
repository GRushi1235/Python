a=int(input("Enter any number"))

def Sumdigits(n) :
    sum=0 
    if n==0 :
        return sum
    else :   
     while n >0 :
        sum = sum + (n % 10)
        n//=10
    return sum    

print("Sum of digits of",a,"is",Sumdigits(a))        