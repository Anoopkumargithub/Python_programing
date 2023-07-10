# Dictionary is nothing but key value pair
d1 = {"Mohit"}
# print(type(d1))
d2 = {"Anoop":"burger", "Skillf":"Roti", "Rohan":"Fish", "Subham":{"B":"maggie", "L":"Roti", "D": "Chicken"}}
# print(d2["Subham"]["B"])
# print(d2["Anoop"])
# d2["Ankit"]  = "JunK Food"  #use for adding key value pair in dicitionary but br can use other methode
# d2[420] = "Kababs"
# del d2[420]     #use to delete the pair
# print(d2)
# d3 = d2.copy()   # it can copy d2 element to d3
# del d3["Anoop"]
# print(d2.copy())
# print(d3)
# print(d2.get("Anoop"))   # it can give value of a perticular key
# d2.update({"Leena":"Toffe"})   # it can update the list 
# print(d2)
# print(d2.keys())  # it can print the keys 
# print(d2.items())   #it can print the items in the list
# print(d2.values())     # it can print the values in the list
# print(dict.fromkeys(d2,d1))   # it can change the key value pair 
# print(d2.setdefault("Subham"))