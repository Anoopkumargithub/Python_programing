a = int(input('Enter the amount'))
if a//2000: 
    x = a//2000
    print("No. of notes of 2000 is\n",x)
    a = a-x*2000
if a//500:
    y = a//500
    print("No. of notes of 500 is\n",y)
    a = a-y*500
if a//100:
    z = a//100
    print('No. of notes of 100 is\n',z)
    a=a-z*100
if a//50:
    v = a//50
    print('No. of notes of 50 is\n',v)
    a=a-v*50
if a//20:
    w = a//20
    print("No. of notes of 20 is\n",w)
    a= a-w*20
if a//10:
    u = a//10
    print("No. of notes of 10 is\n",u)
    a=a-u*10
print("remaing money",a)