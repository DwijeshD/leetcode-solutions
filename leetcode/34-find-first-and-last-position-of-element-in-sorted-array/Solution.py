
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List
    [int]:

        lo, hi = (0, len(nums) - 1)
        ans_left = -1
        ans_right = -1


        while lo <= hi:
            mid = (hi + lo) // 2                

            
            if nums[mid] >= target: