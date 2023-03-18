a = int(input())
b = int(input())
c = 0
if a>=b:
    for i in range(b,a+1):
        c = c+i
    print(c,end=" ")
else:
    for i in range(a,b+1):
        c = c+i
    print(c,end=" ")