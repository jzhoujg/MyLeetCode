class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1,n):
            res = res^(start+2)
            start = start+2
        return res