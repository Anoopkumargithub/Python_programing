Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 15:58:59) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=x=2
y=5
x+y
7
x=9
x+y
14
x
9
y
5
x
9
x+y
14
abc
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'?
x+10
19
19+y
24
_+y
29
y
5
name = 'youtube'
name + 'rocks'
'youtuberocks'
name[0]
'y'
name[6]
'e'
na,e[8]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    na,e[8]
NameError: name 'na' is not defined
name[8]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name[8]
IndexError: string index out of range
name [-1]
'e'
name [-2]
'b'
namee [-7]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    namee [-7]
NameError: name 'namee' is not defined. Did you mean: 'name'?
name [-7]
'y'
name [o:2]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name [o:2]
NameError: name 'o' is not defined
name [0:2]
'yo'
name[1:4]
'out'
name[]1:
    
SyntaxError: invalid syntax
name[1:]
'outube'
name[:4]
'yout'
name[3:10]
'tube'
name[0:3]='my'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    name[0:3]='my'
TypeError: 'str' object does not support item assignment
'my ' + name [3:]
'my tube'
myname = 'anoop kumar'
len(myname)
11
myname = 'anoopkumar'
len (myname)
10
 len (myname)
 
SyntaxError: unexpected indent
len (myname)
10
nums = [25,16,36,95,14]
nums
[25, 16, 36, 95, 14]
nums[0]
25
nums [4]
14
nums [-2]
95
nums [3:]
[95, 14]
names = ['anoop', 'mohit' 'nakukl']
names
['anoop', 'mohitnakukl']
values =[9.5, 'anoop'.25]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
values = [9.5, 'anoop' ,25]
 mil = [nums , names]
 
SyntaxError: unexpected indent
mil = [nums , names]
mil
[[25, 16, 36, 95, 14], ['anoop', 'mohitnakukl']]
nums.append(45)
nums
[25, 16, 36, 95, 14, 45]
nums.insert(2,77)
nums
[25, 16, 77, 36, 95, 14, 45]
nums.remove(14)
nums
[25, 16, 77, 36, 95, 45]
nums.pop(1)
16
nums
[25, 77, 36, 95, 45]
nums.pop()
45
nums
[25, 77, 36, 95]
del nums[2:1]
nums
[25, 77, 36, 95]
del nums[2:]
nums
[25, 77]
nums.extend([29 , 12, 14, 36])
min(nums)
12
max(nums)
77
nums.sort()
nums
[12, 14, 25, 29, 36, 77]
sum(nums)
193




