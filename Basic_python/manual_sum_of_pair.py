

def manual_sum_of_pair(arr):
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[index]:
           index = i

    index2 = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[index] and arr[j] > arr[index2]:
            index2 = j

    return arr[index] + arr[index2]


n = int(input())
s = input().split()
arr = []

for i in range(len(s)):
    arr.append(int(s[i]))

print(manual_sum_of_pair(arr))

#testing e confused : 5 4 3 2 1