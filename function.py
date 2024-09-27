# # # def isGreater(a, b):
     
# # if a > b:
# #         print("a  is the greater number.")
# # else:
# #         print(" d is the greater number or they are equal.")  
        
# # def isGreate(a ,b):
# #         pass
# # a = 19
# # b = 10
# # isGreater(a, b)
# # c = 60
# # d = 70
# # if c > d:
# #         print("a  is the greater number.")
# # else:
# #         print(" d is the greater number or they are equal.")  
 
 
# # # isGreater(a, b)
# # # c = 60
# # # d = 70
# # # isGreater(c, d)

# # # # function call
# # # def fun():
# # #     print("Welcome to GFG")
# # # fun()
# # # # perameters function

# # # def add(num1: int, num2: int):
# # #     """Add two numbers"""
# # #     num3 = num1 + num2
# # #     return num3
# # # # Driver code
# # # num1, num2 = 5, 15
# # # ans = add(num1, num2)
# # # print(f"The addition of {num1} and {num2} results {ans}.")

# # # function farameters 
# # def fl(name):
    
# #     print(name)
      
# # fl("ajju")

# # # squresre
# # def squ(a):
# #     # return a ** 2
# #  a=int(input("enter number=>"))
# # res=squ(a**2)
# # print("result of ",res)
       
#     #    pass by reference 
# # def value(a):
# #     print(id(a))

# #     a=a+20
# #     print(id(a))
# #     print("value a",a)
# # b=1
# # print("value of b",b)
# # print(id(b))

# # # value(b)
# # # print("value od b,,",b)     

# requal args
def area(l,b):
    print("area of rectengle ",l*b)
area(12,23)
    
# keyword args
def data(name, password):
    print("enter you name",name)
    print("enter you password",password)
    
data(name="Ajju",password= 1234)

# defult args
def defaut(a,b,c=5):
    res=a+b+c
    print(res)
defaut(12,2)

# variablle lenght
def sum(*num):
    res = 0
    for i in num:
        res =res + i
    print(res)
    
sum(10, 2)
sum(1, 2, 3)
sum(1, 2, 3, 4)



# # # secend type
# def sum_all(*args):
# 	result = 0
# 	for num in args:
# 		result += num
# 	return result
# print(sum_all(1, 2, 3, 4, 5))


# # # #  decsnary variable lenght
# def sum(n1,**num):
#     res = 0
#     for key in num:
#         res =res+num[key] 
#     print(res)
        
sum(n1=10, n2=2)
sum(n1=1, n2=2, n3=3)
# sum(1, 2, 3, 4)




 