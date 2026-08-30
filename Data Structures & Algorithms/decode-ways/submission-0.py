class Solution:
    def numDecodings(self, s: str) -> int:

        # traverse left to right,
        # take the current digit, map it to a char
        # recurse for the remaining substring
        # append second digit now, recurse for the remaining substring
        # memo results from substrings, to use for multiplying combinatorics results
        # "123 | 456" if 123 can be decoded x ways and 456 y ways then
        #   x * y decodings possible
        #  at index `i` we'll store combinations it can be decoded starting from that string
        # memo[0] would be the result

        self.memo = [0 for _ in range(len(s))]

        def decode(idx):
            # eos case
            if idx == len(s):
                return 1

            # zero case
            if s[idx] == "0":
                return 0

            x = 0
            if idx + 1 < len(s) and self.memo[idx + 1]:
                x = self.memo[idx + 1]
            else:
                x = decode(idx + 1)

            y = 0
            if idx + 1 < len(s) and int(s[idx : idx + 2]) <= 26:
                if idx + 2 < len(s) and self.memo[idx + 2]:
                    y = self.memo[idx + 2]
                else:
                    y = decode(idx + 2)
            self.memo[idx] = x + y
            return x + y

        return decode(0)
