'''
import math
import os
import random
import re
import sys
import socket
import threading
import random
from math import *
'''

# a=append, r=reading, r+=reading and writing

'''
if __name__ == '__main__':
    try:
        value = -0 / 0
        number = int(input("Enter a number : "))
        print(number)
    except ZeroDivisionError as err:
        print(err)
    except ValueError:
        print("Invalid input")
-----------------
if __name__ == '__main__':
       y = int(input("please enter the input : "))
       print("abs1 number is {0}" .format(abs1(y)))
'''

(n, k) = map(int, input().split(' '))

ans = 0

for i in range(n):
    x = int(input())
    if x % k == 0:
        ans += 1

print(ans)
    

    

    