class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0

        for i in nums:
            length = 1
            if i - 1 not in check:
                while i + 1 in check:
                    length += 1
                    i += 1
            longest = max(longest,length)
        return longest
        