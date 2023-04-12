class Solution:
    def simplifyPath(self, __file__: str) -> str:
        return os.path.abspath(__file__)

        stack=[]
        for a in __file__.split('/'):
            if a=='..':
                if stack:
                    stack.pop()
            elif a not in ('','.'):
                stack.append(a)

        return "/"+"/".join(stack) 
