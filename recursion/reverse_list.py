
def reverse_list(a):
    new_list = []
    for i in range(0, len(a)):
        new_list.append(0)
    for i in range(len(a)-1, -1, -1): #start, end, step
        new_list[len(a)-1-i] = a[i]
    
    return new_list


def reverse_list_recursion(a):
    if len(a) == 0:
        return []    
    return [a[-1]] + reverse_list_recursion(a[:-1])

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


list = [1, 2, 3, 4, 5]
print('Normal Data : ', reverse_list(list))
print('Reverse Recursive : ', reverse_list_recursion(list))
print('Fibonacci : ', fibo(6))