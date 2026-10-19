class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        table = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for key,count in count.items():
            table[count].append(key)

        res = []
        for i in range(len(table) -1,0,-1):
            for i in table[i]:
                res.append(i)
                if len(res) == k:
                    return res
        