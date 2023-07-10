def matrix():
    row = int(input())
    coloum = int(input())
    l=[]
    for i in range(row):
        l1= []
        for j in range(coloum):
            x = int(input())
            l1.append(x)
        l.append(l1)
    for i in range(row):
        for j in range(coloum):
            print(l[i][j],end=" ")
        print()

matrix()