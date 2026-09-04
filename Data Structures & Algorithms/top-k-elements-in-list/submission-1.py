class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        
        arr = []

        for num,count in hash_map.items():
            arr.append([count,num])
        
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


