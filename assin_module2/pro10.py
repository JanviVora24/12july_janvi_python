#Write a Python program to get unique values from a list 

list=[1,2,3,4,2,3,5]
list1=[]

for i in list:
    if i not in list1:
        list1.append(i)

print(list1)