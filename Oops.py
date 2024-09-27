class DemoPython:
    a=50
    b=90
    res=a+b
obj=DemoPython()
print(obj.res)

# # method and function working same but defrent only method is class inner
# # and function is class outer and inner create a function def keyword use  
# # yadi class ke under koi function bna rahe hai to function ke under 
# # ek arguments dena need hota hai. 

# # methods & function 
class SeltM:
    b=20
    def show(self):
     print(self.b)
      # self.c=self.b*self.b
         # print(self.c)
    
ab=SeltM()
ab.show()    

# # Inheritance Single
class A:
    def show(self):
        print("parenr Classs==> A")
class B (A):
    # yadi fun. ke under args n likhu to error nhi aaye but parent ka result aayega
    def show2(self):
        print("child Class==> B")
b=B()
b.show()
b.show2()

# maltilevel Inheritance
class A:
    def show(self):
        print("parenr Classs==> A")
class B (A):
    def show2(self):
        print("child Class==> B")
class C (B):
    def show3(self):
        print("child Class==> C")        
c=C()
c.show()
c.show2()
c.show3()

# maltiple Inheritance 
class A:
    def show(self):
        print("Parent Class ==> A")
        
class B:
    def display(self):
        print("Parent Class ==> B")

class C(A, B):
    def introduce(self):
        print("Child Class ==> C")

# Creating an instance of class C
c = C()
c.show()
c.display()
c.introduce() 




                