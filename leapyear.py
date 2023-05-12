# year = int(input("Enter any year to check\nYear is leap or not\n"))
# if year%4==0 and year%400==0:
#     print(bool(1))
# else:
#     print(bool(0))

# def is_leap(year):
#     # leap = False
#     if year%4==0 and year%400:
#         print(leap = "True")
#     # else :
#     #     print(bool(0))
        
#     # Write your logic here
    
#     # return leap

# year = int(input())
# print(is_leap(year))

def is_leap(year):
    leap = False
    if year%400==0:
        return True
    elif year%100 ==0:
        return False
    return leap

year = int(input())
print(is_leap(year))