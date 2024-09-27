# # # a=12
# # # b=23
# # # a,b=b,a
# # # print(a,b)


# # # secend type
# # a,b,c=5,20,30
# # b,c,a=a+5,b-3,c+10
# # print(a,b,c)


# # # thred type
# # x=5
# # y,y=x+10,x-20
# # print(x,y)


# a=10
# b=20

# temp=a
# a=b
# b=temp
# print("a is =",a)
# print("b is =",b)

a=3
b=5

a=a+b
b=a-b
a=a-b
print("a is =",a)
print("b is =",b)


# is not
a = 10
b = 10

print(a is not b) 
print(id(a), id(b)) 

c = "Python"
d = "Python"
print(c is not d) 
print(id(c), id(d)) 

e = [1,2,3,4] 
f = [1,2,3,4] 
print(e is not f) 
print(id(e), id(f)) 
