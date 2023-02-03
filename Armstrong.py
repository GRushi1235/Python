n=int(input("Enter the no to check: "))
sum = 0
count =0
temp = n
while temp>0:
    temp = temp//10
    count=count+1

temp=n
while temp>0:
    digit = temp%10
    sum = sum + digit**count
    temp=temp//10

if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")