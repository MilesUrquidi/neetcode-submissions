class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        check = set(nums)

        for i in nums:
            length = 1
            if (i-1) not in check:
                while i + 1 in check:
                    i += 1
                    length += 1
            longest = max(longest,length)
        return longest   