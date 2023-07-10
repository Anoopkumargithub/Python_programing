# l = 10   #Global scope
# def function1(n):
#     # l = 5  #Local 
#     m = 8   # local
#     global l
#     l = l + 45
#     print(l,m)
#     print(n, " i have printed")

# # print(l)
# function1("This is me")

from re import X

x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    # print("Before calling rohan()",x)
    rohan()
    print("After calling rohan()",x)
    
harry()
print(x)