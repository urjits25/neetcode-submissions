class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        maintain most freq char in the sliding window
        maintain freq counts of chars
        maintain total repl made in the window
        A A A [B A C B B] 
        k = 2
        dict: 
            A : 1
            B : 2
            C: 1
        k = 0
        most_freq = B
        cur_max = 6
        on every change in window length, update most_freq_char
        '''
        if not s:
            return 0
        fm = defaultdict(int)
        l = 0
        cur_max = 0
        cur_count = 0
        res = 0
        for r, c in enumerate(s):
            
            # Add to the freq map
            fm[c] += 1
            cur_count = max(cur_count, fm[c])

            while (r-l+1) - cur_count > k:
                fm[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
                