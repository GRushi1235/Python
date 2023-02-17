def swapPositions(list, pos1, pos2):
 list[pos1], list[pos2] = list[pos2], list[pos1]
 return list 

n = int(input("Enter the size of the array."))
print("enter the elements")
arr = []

for i in range(n):
 element = int(input())
 arr.append(element)

print("enter the positions to swap")
a=int(input())
b=int(input())

print("after swap")


print(swapPositions(arr,a,b))


