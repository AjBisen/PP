# creating list 
l=[]
print(l)
l=[12,23,"hello,'s",34.4]
print(l)
# concatenation usen +
li=[12,23,45,"hello"]
li1=[12,23,32,33]
res=(li+li1)
print(res)
# print(li+li1)

# multiplying Using (repiting )

li=[12,23,34,"hello"]
res=li*3
print(res)

# Membership list (in  or not in=true flase)
li=[1,2,3,4,3]
print(2 in li)
print(5 not in li)
   
# Iteration on lis->list  ki lenth
li=[1,2,22,33,44]
print(len(li))

for i in li:
    print(i)

#deleting list
li=[12,23,34,45,56,67,78]
print(li)

del li[3]
print(li)

li[3]=99
print(li)

# list index 
li=[1,2,3]
li[2]=[2,3,33,34]
li[1]=99
li[0]=(1,2,2,2)
print(li)

# Slicing list 
li=[12,23,32,21,12,22,233]
res=li[2:5]
print(res)

 
 
