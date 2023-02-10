n = int(input("Enter the size of the array."))
print("enter the elements")
arr = []

for i in range(n):
 element = int(input())
 arr.append(element)

print("The sum of the total array are:",{sum(arr)})

