# n = int(input("Enter a no.\n"))
# i =0
# def factorial(n):
#     if i==0 or i==1:
#         return 1
#     else:
#         return n*factorial(n-1)
import math
import os
import random
import re
import sys

def factorial(n):
    # Write your code here

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    if n == 1 or n == 0 :
        return 1
    else:
        return n*factorial(n-1)

    result = factorial(n)
    print(result)



