class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == "D":
                dire.append(i)
            else:
                radiant.append(i)
        while dire and radiant:
            r = radiant.popleft()
            d = dire.popleft()
            if d < r:
                dire.append(d + n)
            else:
                radiant.append(r + n)
        return "Radiant" if radiant else "Dire"
