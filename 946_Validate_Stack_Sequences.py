class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for v in popped:
            # if v is in the stack, then we should be able to pop it immediately
            if v in stack:
                if stack[-1] != v:
                    return False
                else:
                    stack.pop()
            else:
                # if v is not in the stack, push values in pushed[] into the stack till v. 
                # note that, we don't have to push v in the stack if we meet v, because we will need to pop it immediately. 
                while i < len(pushed) and pushed[i] != v:
                    stack.append(pushed[i])
                    i += 1
                i += 1
                
        return True
