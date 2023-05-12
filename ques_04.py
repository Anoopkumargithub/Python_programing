a = int(input("Enter the side of triangle\n"))
b = int(input("Enter the side of triangle\n"))
c = int(input("Enter the side of triangle\n"))
if a+b>c or b+c>a or a+b>c:
    print("Side is valid for triangle")
    if a==b==c :
        print("Triangle isd equilateral")
    elif a==b!=c:
        print("Triangle is isoceleous")
    else:
        print("Triangle is scalene")
else:
    print("side is not valid fpor triangle")