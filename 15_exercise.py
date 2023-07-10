# Faulty Calculator
# 45 * 3 = 555,  56 + 9 = 77 , 56/6 = 47

# num1 = int(input("Enter your number1 "))
# num2 = int(input("Enter your number2 "))
# add = (f"{num1} + {num2} = {num1 + num2} ")
# sub = (f"{num1} - {num2} = {num1 - num2}")
# mul = (f"{num1} * {num2} = {num1 * num2}")
# div = (f"{num1} / {num2} = {num1/num2}" )

# a = [add, sub, mul, div]
# print(input("Enter your sumbol"))
# if a == add:
#     if num1 == 56 and num2 == 9:
#         print("77")
#     else:
#         print(num1+num2)
# elif a == sub:
#     print(num1 - num2)
# elif a == mul:
#     if num1 == 45 or num2 == 3:
#         print("555")
#     else:
#         print(num1*num2)
# elif a == div:
#     if num1 == 56 or num2 == 6:
#         print(47)
#     else:
#         print(num1/num2)
# else:
#     print("invalid input")

x = int(input("Enter your first number:\n"))
print("press + for Additon")
print("press - for subraction")
print("press * for multiple")
print("press / for divide")
a = input()
y = int(input("Enter your secound number:\n"))
if  a== "+" or a == "-" or a =="*" or a=="/":
    if a=="+":
        if x == 56 and y ==9:
            print("77")
        else:
            print(x+y)
    if a=="-":
        print(x-y)
    if a =="*":
        if x ==43 and y ==3:
            print("555")
        else:
            print(x*y)
    if a =="/":
        if x == 56 and y == 6:
            print("57")
        else:
            print(x/y)
else:
    print("invalid format")