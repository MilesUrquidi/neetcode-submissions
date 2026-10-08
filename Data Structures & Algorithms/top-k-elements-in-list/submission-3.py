class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a freq table that counts the amt each number appears. then make buckets for each count and add the numbers for that count, then return the numbers backwards until the len of the result = k

        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1

        for num,cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            

        