class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        start, end = 0, len(people)-1
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            boats += 1
            end -= 1
        return boats
