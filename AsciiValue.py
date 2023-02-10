a=input("Enter any character: ")

def Asciivalueofachar(n):
    if len(n) >1 :
        print("Enter a character not a String")
    else :
       print("Ascii value of",n,"is",ord(n))    
       
Asciivalueofachar(a)      