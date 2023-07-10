# f = open("Anoop.txt", "w")
# a = f.write("Anoop bhai bahut acche hai\n")
# print(a)
# # f.close()
# # f = open('sample.txt','r')
# # f = open('sample.txt')   #  by default 
# # data = f.read()
# # print(data)
# # f.close()

# Handle read and write bith
f = open("Anoop.txt", "r+")
print(f.read())
f.write("Thank you")