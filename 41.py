# def function_name_print(a, b, c, d, e):
    # print(a, b, c, d,e)

def funargs(normal, *args, **kwargs):
    # print(type(args))
    # print(args[0])
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(key, value)

# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The Programmer"]
normal = "This is a normal argument and the students are:"
kw = {"Rohan":"Monitor","Harry":"Fitness Instructor", "The Programer":"Coordinator"}
# funargs(normal, *har, **kwargs)