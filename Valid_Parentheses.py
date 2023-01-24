class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '{':'}','[':']'}
        
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if stack == [] or d[stack.pop()] != i:
                    return False
                  
        return True if stack == [] else False
