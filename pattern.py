a = int(input())
i = 1
space = a-1
while (i<=a):
    print(" "*space+"*"*i+"*"*(i-1)+" "*space)
    i+=1
    space-=1