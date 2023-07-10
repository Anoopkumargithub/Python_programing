n =int(input())
a=0
b=1
print(a,b,end=' ')
i=0
while i<(n-2):
    sum=a+b
    print(sum,end=' ')
    a,b=b,sum
    i=i+1