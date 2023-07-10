#print additon of matrix
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
print()

print("for second matrix")

row =int(input())
col=int(input())
ls2=[]
for i in range (row):
    ls3=[]
    for j in range (col):
        x=int(input())
        ls3.append(x)
    ls2.append(ls3)
print(ls2)
result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(row):    
    for j in range(len(ls[0])): 
        result[i][j] = ls[i][j] + ls2[i][j] 
for r in result: 
    print(r)