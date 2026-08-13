
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> 
    int:

        sorted_points = sorted(points, key=lambda x: x)
        max_gap = 0

        for i in range(len(sorted_points) - 1):
            gap = sorted_points[i][0] - sorted_points[i+1][0]
            max_gap = max(abs(gap), max_gap)

        return max_gap

