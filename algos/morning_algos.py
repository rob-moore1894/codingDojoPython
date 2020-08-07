# Reverse String

# def reverseString(str):
#     newStr = ""
#     for i in range(len(str) - 1, -1, -1):
#         newStr += str[i]
#     print(str)
#     print(newStr)
#     return newStr

# reverseString("I was put on this Earth to be phenomenal!")

# # “String: Is Palindrome
# # Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.”

# def isPalindrome(str):
#     newStr = ""
#     for i in range(0, len(str)//2, 1):
#         if newStr[i] != newStr[len(newStr)-i-1]:
#             return False
#         else:
#             return True


# print(isPalindrome("racecar"))
# print(isPalindrome("false"))

# # Parens Valid
# # Create a function that, given an input string str, returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed. Given "N(0)t )0(k", return false, because the underlined ")" is premature: there is nothing open for it to close.”

# def check(str):
#     open_list = ["[", "{", "("]
#     close_list = ["]", "}", ")"]
#     stack = []
#     for i in str:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else: 
#                 return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False

# print("Y(3(p)p(3)r)s", "-", check("Y(3(p)p(3)r)s"))
# print("N(0(p)3", "-", check("N(0(p)3"))

# # Acronyms
# # Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given " there's no free lunch  -  gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN”

# def acronym(str):
#     phrase_split = str.split()
#     newStr = ""
#     for i in phrase_split:
#         newStr += i[0].upper()
#     print(newStr)

# acronym("Central Intelligence Agency")

# def acro(str):
#     print(''.join(i[0].upper() for i in str.split()))

# acro("Federal Bureau Investigations")

# “Coin Change with Object
# As before, given a number of U.S. cents, return the optimal configuration of coins, in an object.”

#Charles Nesmith, BAB, Carver, Rob Moore

def optimalChange(num):
    quarter = 25
    quarterCount = 0
    dime = 10
    dimeCount = 0
    nickel = 5
    nickelCount = 0
    penny = 1
    pennyCount = 0
    coinChange = {}

    for i in range(num, -1, -1):
        if num >= quarter:
            num -= quarter
            quarterCount += 1
        elif num >= dime:
            num -= dime
            dimeCount += 1
        elif num >= nickel:
            num -= nickel
            nickelCount += 1
        elif num >= penny:
            num -= penny
            pennyCount += 1
    
    coinChange['Quarters'] = quarterCount
    coinChange['Dimes'] = dimeCount
    coinChange['Nickels'] = nickelCount
    coinChange['Penny'] = pennyCount

    print(coinChange)

optimalChange(49)