'''Chef's son wants to go on a roller coaster ride. The height of Chef's son is XX inches while the minimum height required to go on the ride is HH inches. Determine whether he can go on the ride or not.

Input Format
The first line contains a single integer TT - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers XX and HH - the height of Chef's son and the minimum height required for the ride respectively'''
# T = int(input())
# for i in range(T+1):
#     X,H = map(int, input().split())
#     if H>X:
#         print("YES")
#     elif H==X:
#         print("YES")
#     else:
#         print("NO")
# num =int(input())
# for i in range(num):
#     a=input()
#     b=a.split()
#     if int(b[0])>=int(b[1]):
#         print("yes")
#     else:
#         print("no")
a = input()
b = a.split()
if int(b[0]<b[1]):
    print("YES")
else:
    print("NO")