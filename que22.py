# 22. Write a python program that returns the minimum and maximum values in a list of numbers. 
list = [1,2,3,4,7,5]
sorted_list = list.sort()
print(list)
length = len(list)
min = list[0]
max = list[length-1]
print("The maximum element : " , max)
print("The minimum element : " , min)

