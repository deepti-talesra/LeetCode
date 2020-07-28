# Video Explanation: https://www.youtube.com/watch?v=gU8raekRs1E

class Solution:
#         [[1],[2],[3],[]]
#         '''
#         0-->1-->2-->3
#         '''
        
#         [[1,3],[3,0,1],[2],[0]]
#         '''
#                   *
#          +-->0<-->1--+
#          |           |
#          |           |
#          +-->3<------+   
#         '''
    
#     visited = [0,3,1]; stack = []
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)
