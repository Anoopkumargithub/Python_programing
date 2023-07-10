# T = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# sum = a+b+c
# if sum == 180:
#     print("Yes")
# else:
#     print("No")
T = int(input())
while T >0:
    a, b, c = map(int,input().split())
    sum = a+b+c
    if (sum == 180 and a!=0 and b!=0 and c!=0):
        print("Yes")
    else:
        print("No")
    
    T = T - 1