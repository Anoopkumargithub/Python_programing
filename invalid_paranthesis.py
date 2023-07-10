a = "))(("
b = "()())("
a.split()
b.split()
c= a.count('(')
e= b.count('(')
d = a.count(')')
f = b.count(')')
if (e==f):  
    print('valid')
else:
    print('invalid')