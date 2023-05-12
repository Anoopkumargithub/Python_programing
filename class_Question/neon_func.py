def neon():
    x = int(input())
    a = x
    y = x**2
    z = 0 
    for i in range(y):
        z = z+y%10
        y = y//10
    if z==a:
        print("No. is Neon")
    else:
        print("No. is not Neon")

neon()

