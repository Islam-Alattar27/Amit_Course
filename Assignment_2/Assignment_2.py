
##############################################################################################################################################################

# Write a Python program to sum all the items in a list.

x=[1,2,2,3,4,5]
sum=0
for i in x:
    sum+=i
print(sum)


##############################################################################################################################################################

# Write a Python program to get the smallest number from a list.

x=[9,1,8,7,2,0,3,4,5]
x.sort()
print("smallest number from a list is ",x[0])

# #               or              

x=[9,1,8,7,2,0,3,4,5]
print("smallest number from a list is ",min(x))

# #               or              

x=[9,1,8,7,2,0,3,4,5]
small_number=x[0]

for i in x:
    if i < small_number:
        small_number=i
print("smallest number from a list is ",small_number)


##############################################################################################################################################################

# Write a Python program to count the number of strings from a given list of strings.

x=["Islam","Elsayed","Abdelhamed","Ahmed","Alattar"]

print("number of string is",len(x))

# #             or

x=["Islam","Elsayed","Abdelhamed","Ahmed","Alattar"]
count=0
for i in x:
    count+=1
print("number of string is",count)

# #              or

x=["Islam",1,"Elsayed",7,"Abdelhamed",5,"Ahmed","Alattar"]
c=0
for i in x:
    if isinstance(i,str):
        c+=1
        
print("number of string is",c)




##############################################################################################################################################################

# Write a Python program to check if a set is a subset of another set.

x={1,2,3,4,5,6}
y={1,3,5}
z=y.issubset(x)

print(z)

# #                   or

x={1,2,3,4,5,6}
y={1,3,5}
z=y < x

print(z)




##############################################################################################################################################################

# Write a Python program to remove all elements from a given set.

x={1,2,3,4,5,6}

z=x.clear()

print(z)


# #                   or

x={1,2,3,4,5,6}

del x

print(x)




##############################################################################################################################################################

# Write a Python program to unzip a list of tuples into individual lists.

x = [(1,'a'), (2,'b'), (3,'c'),(4,'d')]

numbers, letters = zip(*x)

print(numbers)  
print(letters)  

#                      or

z= [(1, 'a'), (2, 'b'), (3, 'c'),(4,'d')]

x=[]
y=[]

for number,leter in z:
    x.append(number)
    y.append(leter)

print(x)
print(y)



##############################################################################################################################################################

# Write a Python program to reverse a tuple.

x=(1,2,3,4,5,6)

y=x[::-1]

print(y)

#                     or  

x=(1,2,3,4,5,6)

y=reversed(x)

z=tuple(y)

print(z)
