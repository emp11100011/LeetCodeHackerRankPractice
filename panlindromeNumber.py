# Create a program which takes input of a interger and returns true if the integer is palindrome
# 121 is palindrome 123 is not

# Edge Cases/ Quesitons
# Is a unit integer palindrome ?

# Breaking the problem down
# Given a number, we reverse the number and check whether its a palindrome or not
# This can be simply done with the help of string conversion

# If that is not required to solve the problem numerically
# We will extract each unit place and store the remainder into a new number
# We shall do this untill we have extracted each number

# Pseduo Code
# given integer = n
# reverse string = 0
# remainder = 0
# While n > 0:
#     remainder = n % 10
#     reverse = reverse * 10 + remainder
#     n = n/10

# Code
class Sloution:
    def isPalindrome(self, x: int) -> bool:
        revString = 0
        reMain = 0
        checkNum = x
        while x > 0:
            reMain = x % 10
            revString = (revString * 10) + reMain
            x = x // 10
        if checkNum == revString:
            return True
        else:
            return False