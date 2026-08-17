class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s): 
            return ""

        countT = Counter(t)
        
        window = {}
        res, resLen = [-1, -1], float("inf")
        start = 0
        have, need = 0, len(countT)
        
        for end, ch in enumerate(s):
            window[ch] = 1 + window.get(ch, 0)
            if ch in countT and countT[ch] == window[ch]:
                have += 1
            
            while have == need:

                if end-start+1 < resLen:
                    resLen = end-start+1
                    res = [start, end]

                window[s[start]] -= 1
                if s[start] in countT and window[s[start]] < countT[s[start]] :
                    have -= 1
                start += 1
        
        l, r = res
        return s[l:r+1] if resLen <= len(s) else ""