
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left_total = 1
        right_total = 1

        for i in range(len(nums)):
            answer.append(left_total)
            left_total = left_total * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * right_total
            right_total *= nums[i]
