from venv import create


print("Welcome To My Project ")
print("Health Management System")
print("Welcome To Our Health Management Sytstem ")
name = input("Enter Your Name")
f = create("name.txt")
f = open("name.txt", "a")
f.write("Write Your Problem")
