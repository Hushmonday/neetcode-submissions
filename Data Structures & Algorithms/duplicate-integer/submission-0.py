class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di = {}
        for num in nums:
            di[num] = di.get(num, 0) + 1
            if di[num] > 1:
                return True

        return False    