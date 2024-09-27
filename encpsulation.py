''' python provides access to all the variable  and method globally
          ny ussing encpsulation  we can restrict the variable and method acess globally
          by making it pravite or protected'''

class A:
    _a=20 #protected
    __b=30 #pravete
    def show(self):
     print("value of a= ", self._a) 
     print("value of b= ", self.__b)   
a=A()
a.show()

# class name se bhi kar sakte hai( A._a )
print("outside of class= ",a._a)

# print("outside of class= ",a.__b)
