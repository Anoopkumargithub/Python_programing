# a = [1, 2, 3, 4, 5,6 ]
# a[0] = 6
# a[5] = 1
# print(a)
# myvariblecase= "anoop"
# myVariablecase="anooP"
# myVsriableCase="Anoop"
# MyVariableCase="ANoop"
# MYVARIABLECASE="ANOOP"
# print(myVariablecase,myvariblecase,myVsriableCase,MyVariableCase,MYVARIABLECASE)
# Name =("Anoop","Mohit",'Orange')
# a,b,c = Name
# print(a)
# print(b)
# print(c)
# print(a,b,c)
# print(a + b + c)
# x = "awesome"
# def myfunc():
#     print("Anoop is "+x )

# myfunc()
x = "awesome"
def myfunc():
    # global x   
    # ''' due to this the value of x in entier code is equal to good(which is assign in function) 
    # or if you doesn't write printx in function than value of x is equal awesome(which assign out of the function)''' 
    x = "good"
    # print("Anoop is "+x )

myfunc()
print("Anoop is "+ x)