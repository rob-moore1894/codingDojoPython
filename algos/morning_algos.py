# Reverse String

def reverseString(str):
    newStr = ""
    for i in range(len(str) - 1, -1, -1):
        newStr += str[i]
    print(str)
    print(newStr)
    return newStr

reverseString("I was put on this Earth to be phenomenal!")

# “String: Is Palindrome
# Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.”

def isPalindrome(str):
    newStr = ""
    for i in range(0, len(str)//2, 1):
        if newStr[i] != newStr[len(newStr) - 1 - i]:
            return False
        else:
            return True


print(isPalindrome("racecar"))
print(isPalindrome("false"))