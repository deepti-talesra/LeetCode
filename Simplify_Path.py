class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        stack = []
        for d in lst:
            if d == "..":
                if stack:
                    stack.pop()
            elif d != "" and d != ".":
                stack.append(d)
        return "/" + "/".join(stack)
