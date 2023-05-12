## Normal
row = int(input())
coloum = int(input())
l1=[]
for i in range(row):
    l=[]
## Take element from user
    for j in range(coloum):
        x = int(input("enter a no."))
        l.append(x)
    l1.append(l)
# ## print matrix
# for i in range(row):
#     for j in range(coloum):
#         print(l1[j][i],end=" ")
#         # if i==0 or i==2 or j==0 or j==2:
#         #     print(l1[i][j],end=" ")
#         # print()
print("2nd" )
ls=[]
for i in range(row):
    l2=[]
## Take element from user
    for j in range(coloum):
        x = int(input("enter a no."))
        l2.append(x)
    ls.append(l2)

result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(row):
    for j in range(len(l1[0])):
        result[i][j] = l1[i][j] + ls[i][j]
for r in result:
    print(r)
# for i in range (row):
#     for j in range(coloum):
#         print(l1[i][j],end='')
# print()
# for i in range (row):
#     for j in range(coloum):
#         print(ls[i][j],end='')
# print()
# if l1==ls:
#     print("symmetric")
# else:
#     print("asymmetric")