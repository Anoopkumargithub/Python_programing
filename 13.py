# var1 = 6
# var2 = 56
# var3 = int(input("Enter your number"))
# if var3>var2:
#     print("Greater")
# elif var3 == var2:
#     print("Equal")
# else:
#     print("Lesser")
# list = [5, 7, 3]
# print(15 not in list)
# if 5 in list:
#     print("Yes")
# else:
#     print("No")
age = int(input("Enter you age:\n"))
# if age in range(7,100):
#     pass
# else:
#     print("Write your proper age")
if age>100:
    print("You can't drive a vechicle")
elif age<18:
    print("You can't drive a vechicle")
elif age == 18:
    print("we can't take action ,pls go to driving center physically ")
else:
    print("You can drive a vechicle")