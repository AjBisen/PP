# # # age=int (input("enter yor age=> "))
# # # if age>=18:
# # #      print("you can for eligible voting ")
# # # print("you can nat for eligible voting ")

# # if else

# age=int (input("enter yor age=> "))
# if age>=18:
#      print("you can for eligible voting ")
# else:
#   print("you can nat for eligible voting ")
    
# # if elif
# a = 200
# b = 33

# if b > a:
#    print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# # if if elif
    
# a=int(input("enter a value for A=>"))
# b=int(input("enter a value of B=>"))
# c=int(input("enter a value of C=>"))

# if a < b:
#         if a < c:
#             print("value",a)
#         else:   
#           print("value",c)
# else:
#         if b < c:
#             print ("value B=",b)
#         else:
#           print("value",c)
#  #  secend type
        
# a = int(input("Enter a value for A: "))
# b = int(input("Enter a value for B: "))
# c = int(input("Enter a value for C: "))

# if a < b and a < c:
#     print("The smallest value is A =", a)
# elif b < a and b < c:
#     print("The smallest value is B =", b)
# else:
#     print("The smallest value is C =", c)
     
# # nested if 
# age = 38
# if (age >= 11):
#   print ("You are eligible to see the Football match.")
#   if (age <= 20 or age >= 60):
#       print("Ticket price is $12")
#   else:
#       print("Tic kit price is $20")
# else:
#     print ("You're not eligible to buy a ticket.")
 
#secend type 

# a = int(input("Enter a value for A: "))
# b = int(input("Enter a value for B: "))
# c = int(input("Enter a value for C: "))
# d = int(input("Enter a value for D: "))

# if a > b:
#     if a > c:
#         if a > d:
#             print("The greatest value is A =", a)
#         else:
#             print("The greatest value is D =", d)
#     # else:
#     #     if c > d:
#     #         print("The greatest value is C =", c)
#     #     else:
#     #         print("The greatest value is D =", d)
# else:
#     if b > c:
#         if b > d:
#             print("The greatest value is B =", b)
#         else:   
#             print("The greatest value is D =", d)
#     else:
#         if c > d:
#             print("The greatest value is C =", c)
#         else:  
#             print("The greatest value is D =", d)
            
                     
            # result show
# per=int(input("enter you marks=> "))
# if per>90:
#     print("A grade")
#     if per>80 and per<=90:
#         print("B grade")
#         if per >=60 and per <=80:
#             print("C grade")
#             if per>=50 and per<=60:
#                 print("D grade")
#                 if per < 50:
#                     print("fail")
                    
# per = int(input("Enter your marks: "))
# if per > 90:
#     print("A grade")
# elif per > 80:
#     print("B grade")
# elif per >= 60:
#     print("C grade")
# elif per >= 50:
#     print("D grade")
# else:
#     print("Fail")
              
        
                    
 # leap year
year=int(input("enter your year"))
if year%100==0:
    if year%400==0:

        print("enter your leap year ")
    else:
        print("enter your not a leap year")     
    # else:
if year%4==0:
        print("enter yor a leap year")
else:
        print("not leap year")