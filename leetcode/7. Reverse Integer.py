class Solution:
    def reverse(self, x: int) -> int:
        st = str(x)
        if x < 0:
            rev = st[0] + st[1:][::-1]
        else:
            rev = s[::-1]
        r = int(rev)        
        if r < -2**31 or r > 2**31 - 1:
            return 0
        else:
            return r