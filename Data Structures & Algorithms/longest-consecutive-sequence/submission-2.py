class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0

        for num in nums:
            length = 1
            if (num-1) not in check:
                while (num + 1) in check:
                    num += 1
                    length += 1
            longest = max(longest,length)
        return longest
                

        