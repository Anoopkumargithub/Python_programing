x= int(input())
v = (2*x)-1
low =0
high= v-1
value = x
matrix = [[0 for i in range(v) ]for j in range(v)]
for i  in range(x):
    for j in range(low,high +1):
        matrix[i][j] = value
    for j in range(low+1,high+1):
        matrix[j][i] = value
    for j in range(low+1,high+1):
        matrix[high][j] = value
    for j in range(low+1,high+1):
        matrix[j][high] = value
    low = low+1
    high -=1
    value -=1
for i in range(v):
    for j in range(v):
        print(matrix[i][j],end=" ")
    print()
