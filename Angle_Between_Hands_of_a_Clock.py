# Video Explanation: https://www.youtube.com/watch?v=lTPqWStKEyI

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_deg = (minutes*6.0)
        hour_deg = (((hour + minutes/60)/12.0)*360) % 360
        return min(abs(min_deg - hour_deg), 360 - (abs(min_deg - hour_deg)))
