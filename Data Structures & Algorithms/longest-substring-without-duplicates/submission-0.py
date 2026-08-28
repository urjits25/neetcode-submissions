class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window + hashmap with last index in window
        '''
        l = 0
        res = 0
        hm = {}
        for r in range(len(s)):
            c = s[r]
            if c in hm and hm[c] >= l:
                l = hm[c] + 1
            hm[c] = r
            res = max(res, r-l+1)
        return res