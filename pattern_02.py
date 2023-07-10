# # Pattern_01
n=int(input("Enter a no."))
i=0
for i in range(1,n+1):
    print("*"*i)
    i+=1
# # pattern_02
n= int(input("Enter a no."))
i = n 
for i in range(n,1,-1):
    print("*"*i)
    i+=1
# # pattern_03
# n=int(input("Entetr a no."))
i = 0
space=n-1
for i in range(1,n+1):
    print(" "*space + "*"*i)
    i+=1
    space-=1
# #pattern_04
n = int(input("Enter a no."))
i=n+1
space=0
for i in range(n+1,0,-1):
    print(" "*space+"*"*i)
    i-=1
    space+=1
# # Pattern_05
n = int(input("Enter a no."))
i = 0
space=n-1
for i in range(0,n):
    print(" "*space+"*"*i+"*"*(i-1)+" "*space)
    i+=1
    space-=1
# #Pattern_06
n = int(input("Enter a no.\n"))
i=0
space=n
for i in range(1,n):
    print(" "*space+"*"*i+" "*space+"*"*i)
    i+=1
    space-=1
# # Pattern_07
n= int(input("Enter a no.\n"))
i=0
print("*"*(3*n-2))
for i in range(1,n-1):
    i+=1
    space =3*n-4
    print("*"+" "*space+"*")

print("*"*(3*n-2))
# #Pattern_08
n=int(input("Enter a no.\n"))
i=0
x=n-1
space=n-1
s2=2
for i in range(1,n) :
    print(" "*space+"*"*i+"*"*(i-1)+" "*space)
    i+=1
    space-=1
for x in range(n-2,0,-1):
    print(" "*s2+"*"*(x)+"*"*(x-1)+" "*s2)
    x-=1
    s2+=1
#Pattern_09
n = int(input("Enter a no."))
i=0
space = n-2
print(("*")*n)
for i in range(1,n-2):
    print(("*"+" "*space+"*"))
    i+=1
print(("*")*n)
# Pattern_10
n = int(input("Enter a no.\n"))
i = 0
space = 2*n-2
for i in range(1,n+1):
    print("*"*i + " "*space+ "*"*i)
    i+=1
    space-=2
# Pattern_11
n = int(input("Enter a no.\n"))
i = n
space = 0
for i in range(n,0,-1):
    print("*"*i + " "*space+ "*"*i)
    i-=1
    space+=2

