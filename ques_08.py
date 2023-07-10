#check whether matrix is symmetric or not
row =int(input())
col=int(input())
ls=[]
ls2=[]
for i in range (row):
    ls1=[]
    for j in range (col):
        x=int(input())
        ls1.append(x)
    ls.append(ls1)
    ls2.append(ls1)
# print(ls)

for i in range (row):
    for j in range(col):
        print(ls[i][j],end='')
print()
for i in range (row):
    for j in range(col):
        print(ls2[j][i],end='')
print()
if ls==ls2:
    print("symmetric")
else:
    print("asymmetric")