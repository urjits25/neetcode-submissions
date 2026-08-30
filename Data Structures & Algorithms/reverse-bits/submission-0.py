class Solution:
    def reverseBits(self, n: int) -> int:
        binary = []
        for i in range(32):
            if n & (1 << i):
                binary.append("1")
            else:
                binary.append("0")
        
        res = 0
        for i in range(31, -1, -1):
            if binary[i] == "1":
                res |= (1 << (31-i))
        return res