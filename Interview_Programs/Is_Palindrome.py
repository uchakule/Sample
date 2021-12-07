s = input("Enter String Please:")
def is_palindrome(s):
    if s == s[::-1]:
        print('Given string is palindrome')
    else:
        print('Given string is not palindrome')
is_palindrome(s)

