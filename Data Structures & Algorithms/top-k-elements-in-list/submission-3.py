class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for num in nums:
            di[num] = di.get(num, 0) + 1
        
        sorted_nums = sorted(di, key = di.get, reverse = True)
        return sorted_nums[:k]