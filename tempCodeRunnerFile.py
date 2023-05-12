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