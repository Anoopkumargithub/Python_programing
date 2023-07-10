# Pattern printing
# Input = Integer n
# Boolean = true or false

# True n = 5
# *
# **
# ***
# *****

# False n = 5
# *****
# ***
# **
# *
# print("How many rows you want to print")
# a = int(input())
# print("type 1 or 0")
# b = int(input())
# new = bool(b)
# if new == True:
#     for i in range(1,a+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new == False:
#     for i in range(a,0,-1):
#         for j in range(1,i+1):
#             print("*",end = " ")
#         print()

a = int(input("How many rows do you want to print"))
b = int(input("Type 1 or 0"))
new = bool(b)
if new == True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new == False:
    for i in range (a,0,-1):        
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else:
    print("Write 1 or 0 only")

