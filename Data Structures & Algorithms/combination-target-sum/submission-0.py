class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backTrack(start, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backTrack(i, total + nums[i])
                path.pop()
        backTrack(0,0)
        return res