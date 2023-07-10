'''Ques.
Harry got a letter from Hogwarts School to join the wizardry. This letter consists of a magical key (6174) and a 4-digit number n with at least two distinct digits. Harry has to count in how many steps this number n can be converted to magical key invented by professor Dumbledore with this procedure as follows:

1.For number n, create two new numbers x and y consists of the digits in n in ascending and descending order respectively.
2.Subtract the smaller number from the larger number.
Help harry to count the steps to enter in the school.
For example:
N = 1234
Step 1: x = 4321 y= 1234 => n = x-y => 3087
Step 2: x = 8730 y= 0378 => n = x-y => 8352
Step 3: x = 8532 y= 2358 => n = x-y => 6174 
and you are done.

Answer is 3'''
# n = int(input())
n = 1234
#reverse a no.
b=list(map(int, str(n)))
b.sort(key = int, reverse = True)
z = len(b)
c=0
for j in b:
    c=c*10+j
print(c)
for i in range(0,z):
    a=n
    d=c-a
    if d==6174:
        pass
    print(i)