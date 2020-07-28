# Video Explanation: https://www.youtube.com/watch?v=NfiLJi8QRWA

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        blue = len(nums) - 1
        
        while white <= blue:
            curr = nums[white]
            if curr == 0:
                nums[white] = nums[red]
                nums[red] = 0
                red += 1
                white += 1
            elif curr == 1:
                white += 1
            else:
                nums[white] = nums[blue]
                nums[blue] = 2
                blue -= 1
