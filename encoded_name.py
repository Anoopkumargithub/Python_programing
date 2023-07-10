# w1,w2,w3,w4,w5 = map(int, input().split("&"))
# print(w1,w2,w3,w4,w5)
# a=chr(w1)
# b=chr(w2)
# c=chr(w3)
# d=chr(w4)
# e=chr(w5)
# print(a,end="")
# print(b,end="")
# print(c,end="")
# print(d,end="")
# print(e,end="")
a = int(input())
for i in range(0,a+1):
    # print(i,end='')
    for j in range(i+1,2*i+1):
        print(j,end="")
    print()
    i=j