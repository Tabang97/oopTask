def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False
the_string=input("Please enter a string:")
if(is_palindrome(the_string)==True):
    print(the_string, " is a palindrome!")
else:
    print(the_string, " is not a palindrome!")


