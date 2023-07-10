# n = int(input(""))
# if n<=0 :
#     print("Age is not valid, setting age to 0.")
# elif n<13:
#     print("You are young.")
# elif n in range(13,18):
#     print("You are a teenager.")
# else:
#     print("You are old.")

class Person:
    def __init__(self,initialAge):
        print("Age is not valid, setting age to 0.")
        initialAge +=1
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if age in range (-1,13):
            print("You are young.")
        elif age in range (13,18):
            print("You are a teenager.")
        else:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        print("You are old.")
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")