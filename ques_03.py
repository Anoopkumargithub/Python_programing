a = int(input("enter the variable of x^2\n"))
b = int(input("enter the variable of x\n"))
c = int(input("enter the constant term\n"))

D = ((b**2) - 4*a*c)
if D<0:
    print('roots are complex')
    print(D)
elif D>0 :
    print("roots are real")
    print(D)
elif D==0 :
    print("roots are real and equal")
    print(D)
else:
    print("Enter no. only")

x = ((-b + (D)**0.5)/2*a)
y = ((-b - (D)**0.5)/2*a)
print("roots are\n",(x,y))