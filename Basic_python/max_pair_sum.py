# problem name : Find the maximum pair sum in a given array of integers

def max_pair_sum(arr):
    max_data = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)): # j = i+1; j < len(arr); j++
            max_data = max(max_data, arr[i] * arr[j])
    return max_data


n = int(input())
s = input().split()
arr = []
for i in range(len(s)):
    arr.append(int(s[i]))

print(max_pair_sum(arr))
# print(arr)