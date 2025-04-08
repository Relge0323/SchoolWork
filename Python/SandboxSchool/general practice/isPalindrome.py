# write a program that returns True if a word is a palindrome and false otherwise



def isPalindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    

    return isPalindrome(s[1:-1])
    



s1 = '121'
s2 = '111'
s3 = '1234321'
s4 = 'bob'
s5 = 'step on no pets'




print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))
print(isPalindrome(s4))
print(isPalindrome(s5))