def armstrong(x):
    y = 0
    z = x
    while z > 0:
        a = z % 10
        y += a ** n
        z //= 10
    if x == y:
        print(x,"is an Armstrong number")
    # else:
    #     print(x,"is not an Armstrong number")
x = input()
n = len(x)
x = int(x)
i=0
for i in range(x):
    if armstrong(i):
        i=i+1