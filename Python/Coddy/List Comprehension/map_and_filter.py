words = eval(input())  # Don't change this line

# method that takes a string and returns True if the string is the same forwards and backwards.
# else return False
def isPalindrome(astring):
    if len(astring) <= 1:
        return True
    if len(astring) > 1:
        if astring[0] == astring[-1]:   # comparing the first and last char in the string
            return isPalindrome(astring[1:-1])  # using recursion to return the unchecked portion of string
    return False


# creating a new list and appending the first letter of a word if it is a palindrome
new_words = [word[0] for word in words if isPalindrome(word)]

print(new_words)
