
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window
        left = 0
        right = 0
        seen = set()
        best = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1