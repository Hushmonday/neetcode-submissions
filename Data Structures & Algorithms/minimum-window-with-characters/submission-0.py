class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        di = {}
        wind = {}
        for ch in t:
            di[ch] = di.get(ch, 0) + 1
        
        have = 0
        need = len(di)
        l = 0
        reslen = float("inf")
        res = [-1, -1]

        for r in range(len(s)):
            wind[s[r]] = wind.get(s[r], 0) + 1
            if s[r] in di and wind[s[r]] == di[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                wind[s[l]] -= 1

                if s[l] in di and wind[s[l]] < di[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if reslen != float("inf") else ""
