def linear_search(some_list, value):
    for i in range(len(some_list)):
        if some_list[i] == value:
            return "Data Found"
    
    if i == len(some_list) - 1:
        return "NOT Found"


def binary_search(data, value):
    if value > data[-1]:  # negative value will be return
        return "Not Found"
    
    first = 0
    last = len(data)

    while first <= last:
        mid = (first+last) // 2

        if data[mid] == value:
            return "Found"
        elif data[mid]>value:
            first=mid+1
        elif data[data]<value:
            last=mid-1

    if first > last:
        return "Not Found"
    



a = [3, 2, 1, 5, 4, 10, 9, 8, 7]
n = int(input('what you want to search : '))
print(linear_search(a, n))

x = int(input('what you want to search : '))
print(binary_search(a, x))