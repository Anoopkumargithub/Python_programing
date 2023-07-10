#print boundary of the matrix
row =int(input())
col=int(input())
ls=[]
for i in range (row):
    ls1=[]
    for j in range (col):
        x=int(input())
        ls1.append(x)
    ls.append(ls1)
print(ls)
for i in range (row):
    for j in range(col):
        if i==0 or i==2 or j==0 or j==2:
            print(ls[i][j],end='')
        else :
            print()
print()