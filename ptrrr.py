# no = int(input("Enter the number of rows: "))  
# for num in range(no+1):  
#         for i in range(num):  
#             print(num, end=" ")       
#         print()

# the given number Amstrong 

number=int (input("enter any number==>"))

number = str(number)
string_length = len(number)
sum = 0

for i in number:
    sum += int(i)**string_length
    
if sum == int(number):
    print(" given number",number,"is an Amstrong number.")
else:
    print("given number",number,"is Not an Amstrong number.")
    
#     # input string from user Reverse

# given_string = (input("any name type"))
# reverse_string = ""

# for i in given_string:
    
#     reverse_string = i + reverse_string  
    
# print(reverse_string)

# # # given string pilindrom
# name = "madam"
# reverse_string = ""
# for i in name:
#     reverse_string = i + reverse_string  
# if(name == reverse_string):
    
#    print("The string", name,"is a Palindrome.")
   
# else:
#    print("The string",name,"is NOT a Palindrome.")
   