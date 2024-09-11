class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                last = stack.pop()
                if last > -ast:
                    stack.append(last)
                    break
                elif last == -ast:
                    break
            else:
                stack.append(ast)
        return stack
