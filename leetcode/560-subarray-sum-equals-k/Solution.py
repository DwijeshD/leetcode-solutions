
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        prefix = 0
        counter = 0

        for i in range(len(nums)):
            prefix += nums[i]
            needed = prefix - k
            if needed in map:
                counter += map[needed]
            map[prefix] = map.get(prefix, 0) + 1

        return counter