print("Pattern_01")
n = int(input("Enter a no.\n"))
i =0
for i in range(1,n+1):
    print("*"*i)
    i+=1
print("Pattern_02")
i = n
for i in range(n,0,-1):
    print("*"*i)
    i-=1
print("Pattern_03")
i =0
for i in range(1,n+1):
    print("*"*i)
    i+=1
i = n
for i in range(n-1,0,-1):
    print("*"*i)
    i-=1
print("Pattern_04")
i=0
space=4
for i in range(1,n+1):
    print(" "*space+"*"*i)
    i+=1
    space-=1
print("Pattern_05")
i=n
space=4
for i in range(n,0,-1):
    print("*"*i+" "*space)
    i-=1
    space+=1
print("Pattern_06")
i=0
space=n
for i in range(1,n):
    print()
print("Pattern_")
n=int(input("enter a no."))
i=0
space=n
for i in range(1,n+1):
    print(" "*space+"*"*i)
    i+=1
    space-=1

i=n
space=0
for i in range(n,0,-1):
    print("*"*i+" "*space)
    i-=1
    space+=1