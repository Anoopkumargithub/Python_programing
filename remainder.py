n1,n2=  map(eval, input().split())
if n1>n2:
    a = n1//n2
    rem = n1-(a*n2)
    print(rem)
elif n2>n1:
    a=n2//n1
    rem = n2-(a*n1)
    print(rem)
elif n1==n2:
    print("0")