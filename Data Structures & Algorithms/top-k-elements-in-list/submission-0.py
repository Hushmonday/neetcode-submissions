class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        di = {}
        res = []
        for num in nums:
            di[num] = di.get(num, 0) + 1
            
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in di.items():
            bucket[freq].append(num)

        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
            if len(res) == k:
                return res