class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            pair = numbers[low] + numbers[high]
            if pair == target:
                return [low + 1,high + 1]
            elif pair < target:
                low += 1
            else:
                high -= 1
        return []