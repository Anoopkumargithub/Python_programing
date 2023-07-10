row = int(input())
column = int(input())
l= []
for i in range(row):
    l1=[]
    for j in range(column):
        x = int(input())
        l1.append(x)
    l.append(l1)
for i in range(row):
    for j in range(column):
        print(l[j][i],end = " ")
    print()

(n,x) = map(int,input().split())
a = (2**x)
z =a
for j in range(n+1):
    b = z/2
    c = (z-b)
    z = c/2
        
print(c)