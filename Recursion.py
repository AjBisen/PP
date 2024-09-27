''' A  function colling itself again and again to cumputer 
a value is referred to Recursion function or Recursion (1000bar set milit call karta hai ) '''
def Rec():
    print("Hello python")
    Rec()
Rec()

#  secend type
i=0
def rec():
    # i=0
    global i
    i=i+1
    print("hello",i)
    rec()
rec()
# (set by difault and user difaind)
# -----------------------
import sys
print(sys.getrecursionlimit ())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

