n = int(input("enter a no.\n"))
last = n%10
count = 0
while n>=10:
   n = n//10
   first = n

sum = first +last
print(sum)
