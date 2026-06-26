

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        reverse_s = ""
        if s[0] == '-':
            reverse_s = "-" + "".join(reversed(s[1:]))
        else:
            reverse_s = "".join(reversed(s))
        res = int(reverse_s)
        if not (-2**31 <= res <= 2**31 - 1):
            return 0
        return res