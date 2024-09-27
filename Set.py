s1={12,23,34,45,56,67,12,22,33,}

c={}
print(type(c))

print(s1)
# print(id(s1))
# print(type(s1))

for a in  s1:
    print(a)
    
    
print("...function of set .........")
print(set(s1))

print(".........remove.......")
s1.remove(23)
print(s1)   
 
#  not show error not eliment 121
print("...descard....")
s1.discard(121)
print(s1)

# not use index number use
print("...pop.......")
print(s1.pop())
print(s1)

print("...update.....")
# update
a={11,22,23}
b={11,44,55,66}
b.update(a)
print(b)

print("...creal.....")
ss={12,23,45,67,}

ss.clear()
print(ss)

print("...Add....")

ss.add(232)
print(ss)