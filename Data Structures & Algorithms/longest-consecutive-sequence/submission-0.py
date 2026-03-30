class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        best = 0
        for i in n:
            if i-1 not in n:
                cur = i
                length = 1
                while cur + 1 in n:
                    length += 1
                    cur += 1
                best = max(best, length)
        return best