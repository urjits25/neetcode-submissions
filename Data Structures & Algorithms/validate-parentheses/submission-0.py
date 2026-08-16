class Solution:
    def isValid(self, s: str) -> bool:
        '''
        maintain stack of open brackets
        close them in top bracket first order ==> valid
        '''
        stack = []
        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for b in s:
            if b in pairs:
                if stack and stack[-1] == pairs[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return False if stack else True
            