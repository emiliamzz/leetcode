class Solution:
    def reverseBits(self, n: int) -> int:
        b = list("{0:b}".format(n))
        b.reverse()
        while len(b) < 32:
            b.append('0')
        return int(''.join(map(str, b)), 2)