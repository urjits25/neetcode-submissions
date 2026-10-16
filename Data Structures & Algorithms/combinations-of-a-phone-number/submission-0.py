class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_alpha = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return []
        res = []
        def dfs(i, cur_res): 
            if i == len(digits):
                res.append("".join(cur_res) )
                return 
            
            for c in dig_alpha[digits[i] ]:
                cur_res.append(c)
                dfs(i+1, cur_res)
                cur_res.pop()
        
        dfs(0, [])
        return res