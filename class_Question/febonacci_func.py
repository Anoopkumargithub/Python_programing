def febonacci():
    a = 0
    b = 1
    print(a,end="")
    for i in range(10):
        a=a+b
        b=a
        print(b,end="")
febonacci()