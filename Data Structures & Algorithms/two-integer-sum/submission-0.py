class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in di:
                return [di[diff], i]
            di[num] = i