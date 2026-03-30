class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        di = {}
        for ch in s:
            di[ch] = di.get(ch, 0) + 1

        for ch in t:
            if ch not in di or di[ch] == 0:
                return False
            di[ch] -= 1
            
        return True
