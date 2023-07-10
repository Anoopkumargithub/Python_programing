# n = int(input("Enter a no."))
# # # i = 1
# # # while i<n:
# # #     print(i)
# # #     i = i+1
    
# for i in range(0,n+1):
#     print(i**2)
# # i = 0
# # if n<=20:
# #     while i>=n:
# #         print(i**2)
# #     i = i+1
# # else:
# #     pass
# if 1<=n<=20: 
#     i=0
#     while i<n:
#         print(i**2)
#         i=i+1
# else:
#     pass
n = int(input().strip())
i=0
for i in range(1,n+1):
    print(f"{n}x{i} = {n*i}")
    i = i+1
