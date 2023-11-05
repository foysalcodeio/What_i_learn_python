password_bank = {
    'foysal' : '3210',
    'hridoy' : '01790',
    'rakib' : '2365'
}

matched = False
x = 0
print('Enter your username ')

while x < 3:
    username = input()
    if username in password_bank:
        for i in range(0, 3):
            print("Enter your password ")
            password = int(input())
            if password in list(password_bank.values()):
                matched = True
                print('Login successful')
                break
            
    else:
        print('Try Again .... ')

    x+=1

    if matched:
        break
