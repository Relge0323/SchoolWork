def isPalindrome(num):
    lst = str(num)

    if len(lst) <= 1:
        return True
    
    if lst[0] == lst[-1]:
        new_num = int(lst[1:-1])
        return isPalindrome(new_num)
    
    return False




# Test cases
print(isPalindrome(12321))  # True
print(isPalindrome(12322))  # False
print(isPalindrome(5))      # True
print(isPalindrome(32))     # False
print(isPalindrome(676))    # True