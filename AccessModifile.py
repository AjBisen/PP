class A:
    a=10
    _b=20
    __c=22
    print(a,"  ",_b,"  ",__c,"  ")
    def Add(self):
        self.__c=self.a+self._b
        print("Addition ",self.__c)
        
ab=A()
ab.Add()

# print(ab.a)
# print(ab._b)
# print(ab.__c)

class B(A):   
    pass  
    # def show(self):
obj=B()

print(obj.a)
print(obj._b)
print(obj.__c)
