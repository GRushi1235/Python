a=float(input("Enter the length of triangle:"))
b=float(input("Enter the Breadth of tringla:"))

def area(l,b):
    if (l > 0.0 and b > 0.0 ) :
        area = 0.5 * l * b
        print("Area of Triangle with length",l,"and breadth",b,"is",area)
    else: 
        print("enter valid length length or breadth")
             
area(a,b)    