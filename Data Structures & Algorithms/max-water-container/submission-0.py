class Solution:
    def maxArea(self, height: List[int]) -> int:
        """use two pointers, one at start, one at end
        keep the bigger pointer and move in from the smaller one, keep a total tracker
        that tracks the width (index) times the min height. then take the max after each pointer look
        """
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            count = 0
            length = r - l
            high = min(height[l],height[r])
            count = length * high
            res = max(res,count)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return res

        