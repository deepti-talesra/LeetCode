class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            self.visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)
            return 
        province = 0
        self.visited = set()
        n = len(isConnected)
        for i in range(n):
            if i not in self.visited:
                province += 1
                dfs(i)
        return province
