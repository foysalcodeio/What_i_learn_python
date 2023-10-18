
import math
import os
import random
import re
import sys
import socket
import threading
import random
from math import *


def print_odd(data):
    new_list = []
    for i in range(len(data)):
        if (data[i]%2)!=0:
            new_list.append(data[i])

    return new_list



if __name__ == '__main__':
    value = []
    print("Enter the range : ")
    target = int(input())

    print("Enter the data : ")
    for i in range(target):
        x = int(input())
        value.append(x)
    print(print_odd(value))


# val = [1, 2, 3, 4, 5]
# print(print_odd(val))
