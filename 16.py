# list1  =[   ["Anoop",2],    ["Mohit",4],    ["Aashi",3],    ["Heer",9]]
# # print(list1[0], list1[1], list1[2],list1[3])
# dict1 = dict(list1)
# # print(dict1)
# # for item, loolypop in dict1.items():
#     # print(item,"priya", loolypop)
# for item in dict1:
#     print(item)

items = [int , float ,"AnOOp",5, 3, 3, 22, 21, 64 , 23 , 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)