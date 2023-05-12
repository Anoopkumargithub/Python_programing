# n = int(input("Enter a no.\n"))
# n = (bin(n)[2:])
# n = str(n)
# print(n)
# sl = sorted(n)
# print(sl)
# print(n.count('1'))
check_consecutive=(["a","a","a","a","a","a",2,3])
def check_consecutive(lst):
 count = 0
 for i in range(len(lst)-1):
     if lst[i] == "a" or lst[i+1] == "a":
         count +=1
     elif lst[i+1] - lst[i] == 1:
         count +=1
 if count == len(lst)-1:
     return True
 return False