class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i,j in enumerate(nums):
            diff = target - j

            if diff in track:
                return [track[diff],i]
            
            track[j] = i