a='Hello'
b="User"
c='''  How are you,
wlcm to my prograam
in this progran you can 
learn about the string '''
d="""This is use for 
multiline string
above string also used for 
multiline string"""
print(a[1]) #[] use for arrays in string
print(len(b))
print("wlcm" in c) # use to check the word is present in the string
print("wlcm" not in d)
print("use" not in d)
print(c[2:5])
print(c[:5])
print(c[2:])
print(c[-9:-2])
print(a.upper()) #use to capitalize the strting
print(b.lower()) #use to lowerize the strting
print(c.strip()) #use to remove whitespace from the front
print(a.replace("H","a")) #use to replace words in the string
print(c.split())  #use to convert string in to list
print(a+b+c) #use to add 2 or more variable
print(a+" "+b+" "+c) #use to add spce btween a&b
age = 44
z = "My name is.... and i am  {}"
y = "My name is.... and i am  {} {} {}"
print(z.format(age))
print(y.format(age,a,b,z))