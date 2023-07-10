#print upper half of the matrix
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
        if i<=j:
            
            print(ls[i][j],end='')
print()