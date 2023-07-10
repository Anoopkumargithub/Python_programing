num = int(input("Enter a no.\n"))
# print(str(num)[::-1])
a = num%10
print(a)
num = num-a
b = num%100
print(b)
num = num-b
print(num)
c = num%1000
print(c)
print(a*1000+b*100+c*10)