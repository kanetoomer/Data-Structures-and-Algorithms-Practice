'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
'''

# Problem Link: https://neetcode.io/problems/validate-parentheses

# What do I need to do?
'''
Concatenate two strings. Need to create an array "ans" that is two times "n".
'''

# How should I approach this problem?
'''
Understand the problem constraints.
- Need to create a new array "ans" of length 2n, where:
    + the first half of "ans" (indices 0 to n-1) is the same as the input array "nums".
    + the second half of "ans" (indicies n to 2n-1) is also the same as "nums".
'''

#1. Brute Force | Time Complexity - O(n^2)  | Space Complexity - O(n)
def isValid(self, s: str) -> bool:
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
    return s == ''

# 2. Stack | Time Complexity - O(n)  | Space Complexity - O(n)
def isValid(self, s: str) -> bool:
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False