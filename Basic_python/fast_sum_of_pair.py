
#This is a snippet from fast_sum_of_pair.py
#this algorithm work on O(1)

def sum_data(a, b):
    return a + b

def fast_sum_of_pair(arr):
    index = 0
    dup_rem = list(set(arr)) # duplicate data remove
    dup_rem.sort();
    first_large = dup_rem[-1]
    two_large = dup_rem[-2]
    print(sum_data(first_large, two_large))



n = int(input())
s = input().split()
arr = []
for i in range(len(s)):
    arr.append(int(s[i]))

fast_sum_of_pair(arr)