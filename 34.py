# # def print2(str1):
# #     print2(str1)
# #     print("This is " + str1)

# # print2("harry")
# def  factorial_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#     return fac
#     """
#     :param n: Integer
#     :return: n*n-1 * n-1 * n-2 * n-3__________   
#     """
#     pass

# number = int(input("Enter the number"))
# print("Factorial using Iteratiive Method", factorial_iterative(number))
# def factorial_recursive(n):
#     if n ==1:
#         return 1
    
#     else:
#         return n * factorial_recursive(n-1)

# number = int(input("enter your number"))
# print("factorial using recursive method", factorial_recursive(number))
    
def fibonacchi(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacchi(n-1) + fibonacchi (n-2)

num = int(input("Enter your number"))
print("Fibonacchi number ", fibonacchi(num))