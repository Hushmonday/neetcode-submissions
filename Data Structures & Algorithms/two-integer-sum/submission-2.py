class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in di:
                return [di[comp],i]
            di[num] = i