'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(c)

                case ')' | ']' | '}':
                    if len(stack) is 0:
                        return False
                    
                    top = stack.pop()
  
                    if c is ')' and top is not '(':
                        return False
                    
                    elif c is ']' and top is not '[':
                        return False
                    
                    elif c is '}' and top is not '{':
                        return False

                case _:
                    return False
        
        if len(stack) is not 0:
            return False

        return True

