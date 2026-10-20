class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)

        length = 0
        for num in nums:
            if (num -1) in check:
                continue
            reach = num
            while reach + 1 in check:
                reach += 1
            length = max(length, reach - num + 1)
        return length
            

        





        