class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]
        max_len = 1
        for num in nums[1:]:
            if num > lst[-1]:
                lst.append(num)
                max_len += 1
            else:
                left, right = 0, len(lst) - 1
                while left < right:
                    mid = (left + right)//2
                    if lst[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                lst[left] = num
        return max_len
