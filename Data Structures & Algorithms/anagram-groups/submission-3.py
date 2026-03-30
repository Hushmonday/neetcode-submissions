class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in di:
                di[key] = []
            di[key].append(s)
        return list(di.values())