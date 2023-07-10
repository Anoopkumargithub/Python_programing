with open("Anoop.txt","rt") as f:
    a = f.readlines()
    print(a)

f = open("Anoop.txt","rt")
print(f.readlines())
# print(f.readline())

f.close()