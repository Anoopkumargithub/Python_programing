# n = int(input())
# b = int(input())
# blank=0
# a=1
# space=(n-1)
# for i in range(n):
#     print(" "*space+"*"*(a)+" "*blank+"*"*(a)+" "*space)
#     # if i==b:
#     #     blank=0
#     #     star=i
#     #     print(" "*space+"*"*(a)+" "*blank+"*"*star+"*"*(a)+" "*space)
#     space=space-1
#     blank=blank+2 
rows=int(input())
a = int(input())
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==a:
            print("*",end="")
        else:
            print(" ",end="")
    print()