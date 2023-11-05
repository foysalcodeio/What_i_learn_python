def remove_duplicate(data):
    return list(set(data))

if __name__ == '__main__':
    data = input()
    print(remove_duplicate(data))