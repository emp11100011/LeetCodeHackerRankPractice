'''
from audioop import reverse
from venv import create


class Solution:
    def isValid(self, s: str) -> bool:
        copyStr = s
        workingStr =copyStr[:int((len(copyStr)/2))] 
        checkStr = copyStr[int((len(copyStr)/2)):]
        paranDict = {
            '(': ')',
            '{': '}',
            '[': ']',
            ')': '(',
            ']': '[',
            '}': '{'
        }
        createStr = ''
        for paran in workingStr:
            for k,v in paranDict.items():
                if paran == k:
                    createStr = createStr + v
        createStr = createStr[::-1]
        if checkStr == createStr:
            return True
        else:
           return False

s = Solution()
s.isValid("()[]{}")
'''
# Python discussion board solution official
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack



'''
# Python discussion board solution comments
def isValid(self, s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []
'''
class Solution:
    def isValid(self, s: str) -> bool:
        closingBracket = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in closingBracket:
                print(char)
                element = stack.pop()
                print(element)
                print('Closing Bracket [char] = ', closingBracket[char])
                if closingBracket[char] != element:
                    return False
            else:
                stack.append(char)
        return not stack
s = Solution()
s.isValid("()[]{}")