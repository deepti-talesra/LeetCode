class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        connection = set()
        for start, end in connections:
            neighbors[start].append(end)
            neighbors[end].append(start)
            connection.add((start, end))
            
        curr = [0]
        reverse = 0
        visited = set()
        visited.add(0)
        
        while curr:
            new_curr = []
            for city in curr:
                for n in neighbors[city]:
                    if n not in visited:
                        visited.add(n)
                        if (n, city) not in connection:
                            reverse += 1
                        new_curr.append(n)
            curr = new_curr
        return reverse
