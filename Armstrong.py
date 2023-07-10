# x = int(input())
# # n = len(x)
# # x = int(x)
# y = x
# a = 0
# for i in range (1,x+1):
#     z = x%10
#     a = a+z**3
#     x = x//10
# if x==a:
#     print("Armstrong")
# else:
#     print('Not')
def arm():
    x = (input())
    n = len(x)
    x=int(x)
    y = 0
    z = x
    while z > 0:
        a = z % 10
        y += a ** n
        z //= 10
    if x == y:
        print(x,"is an Armstrong number")
    else:
        print(x,"is not an Armstrong number")
arm() 