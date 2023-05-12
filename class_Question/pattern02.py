ls=[]
for i in range(0,3):
    x = list(input())
    ls.append(x)
for i in range(0,3):
    for j in range(0,3):
        if i+j<2:
            print(ls[i][j],end = ' ')
for i in range(0,3):
    for j in range(0,3):
        if i+j==2:
            print(ls[j][i],end="")
for i in range(0,3):
    for j in range(0,3):
        if i+j>2:
            print(ls[i][j],end = "")