# 2. Write a python program to read two lists color-list1 and color-list2. Print out all colors
#from color-list1 not contained in color-list2.


list1 = input("Enter colors in list1(seperated with space): ").split()
list2 = input("Enter colors in list2(seperated with space): ").split()
result = []
for color in list1:
 if color not in list2:
  result.append(color)
  print(result)