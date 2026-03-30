class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for word in strs:
            key = "".join(sorted(word))
            
            if key not in di:
                di[key] = []
            
            di[key].append(word)
        return list(di.values())