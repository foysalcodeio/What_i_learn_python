
phone = ['iphone', 'oppo', 'ASUS', 'motorola', 'nokia']

print('Enter a tech name : ')
name = input()
if name not in phone:
    print("your phone is not collected")
else:
    print(name + ' is found')
