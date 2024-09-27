'''polymorphism means same function name (but different signature )
beging uses for difrent type '''

# function name same but paramiter(signature) change-function overloading
''' whenever class contains more then one method with same name and deffrent types 
    parameter colled overloading'''
    
# lis=[12,23,34,45.56]
# print(len(lis))
# list1="python"
# print(len(list1))

class Ploymorphis:
    
    
    def poly(self):
     print("enter any name ")
     
    def poly(self,name=''):
     print("enter any name ",name)
     
    def poly(self,name='',lastname=''):
     print("enter any name ",name,lastname)

po=Ploymorphis()
po.poly()
po.poly("ajju")
po.poly("ajay", "pawar")
# po.poly('xyz')

# function name same but defrent class me - function overwriding 

# class Ploymorphis:
#     def poly(self):
#        print("this is parent class")
        
# class over(Ploymorphis):
#     def poly(self):
        
#         #  super().poly()
         
#          print("this is child class")
# ov=over()
# ov.poly()
        