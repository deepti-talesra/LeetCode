class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, value in enumerate(values):
            n, d = equations[i]
            graph[n][d] = value
            graph[d][n] = 1/value

        def dfs(node, target, curr, visited):
            if node not in graph or target not in graph:
                return -1
            if node == target:
                return 1
            if target in graph[node]:
                return curr * graph[node][target]
            visited.add(node)
            for connection in graph[node]:
                if connection not in visited:
                    result = dfs(connection, target, curr*graph[node][connection], visited)
                    if result != -1:
                        return result
            return -1

        for n, d in queries:
            output.append(dfs(n, d, 1, set()))
        return output
