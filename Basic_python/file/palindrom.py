
import math
import os
import random
import re
import sys
import socket
import threading
import random
from math import *

if __name__ == '__main__':
    f = open('NUMBERS', 'w+')
    f.write('123321')
    f.close()

    f = open('NUMBERS', 'r+')
    data_list = list(f.read())
    # print(data_list)
    f.close()

    is_palindrome = True

    for i in range(int(len(data_list)/2)):
        if data_list[i] != data_list[len(data_list)-i-1]:
            is_palindrome = False
    
    if is_palindrome:
        f = open('NUMBERS', 'a')
        f.write('YES')
        f.close()
    else:
        f = open('NUMBERS', 'w')
        for i in range(len(data_list)):
            f.write('0')

    
    

