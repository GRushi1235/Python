n = int(input("Enter the size of list"))
list = []
print("enter the elements")
for i in range(n):
 element = int(input())
 list.append(element)
 
print("the no of elements in list are",len(list)) 
r = int(input("Enter pos to remove an element"))
list.pop(r)
list.sort()
print("sorted list is ")
print(list)
list.reverse()
print("revers order of list is")
print(list)
print("min element is ",min(list))
print("max element is ",max(list))
