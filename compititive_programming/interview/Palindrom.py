
def is_palindrome(word):
    return word == word[::-1]

if __name__ == '__main__':
    data =  input()
    if(is_palindrome(data)):
        print("Yes")
    else:
        print("No")