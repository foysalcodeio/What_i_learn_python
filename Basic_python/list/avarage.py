
import math
import os
import random
import re
import sys
import socket
import threading
import random
from math import *

def center_avg(data):
    total = 0
    cnt = 0
    temp_data = data.sort()
    for i in range(1, len(data)-1):
        total = total + data[i]
        cnt = cnt + 1
    return int(total/cnt)
        

if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(center_avg(a))