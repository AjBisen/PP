# for i in range(1,10):
#   print("ajju",end="  ")
  
  # given string
given_string = "madam"
reverse_string = ""

for i in given_string:
    reverse_string = i + reverse_string  
    
if(given_string == reverse_string):
   print("The string", given_string,"is a Palindrome.")
else:
   print("The string",given_string,"is NOT a Palindrome.")
  
# number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# # We are using "for loop" to iterate the multiplication 10 times       
# print ( number)    
# for count in range(1, 11):      
#    print (number, 'x', count, '=', number * count)    
   
   
# #    2 to 10
# for i in range(1,11):
#     print((i))
#     for j in range(1,11):
#         print("%-d X %d = %d" % (i, j, i*j))
        
        # for loo + else
li=[1,2,3,4,]
for i in li:
  print(i)   
else:
    print("done") 
     
# break statment
for i in range(1,30):
    print(i)
    if(i==3):
     break
 
#  Continue Statment
for i in range(9):
  if i == 3:
    continue
  print(i)
  
#   secend type
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)

# Pass Statement
n = 10
if n > 10:    
  print('Hello')
  pass

# secend type break name 
name=input(("enter name"))
for i in name:
  if(i==' '):
    break
  # continue
  print(i, end='')
  