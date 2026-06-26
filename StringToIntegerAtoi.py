class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()

        if(not s or (s[0] not in ["-", "+"] and not s[0].isdigit())):
            return 0
        sign = 1
        if s[0] in ["-", "+"]:
            if s[0] == "-":
                sign = -1
            s = s[1:]
        
        for char in s:
            if not char.isdigit():
                print(char)
                s = s[:s.index(char)]
                break
        res = int(s) if len(s) > 0 else len(s)
        print(res)
        return max(-2**31, min(sign * res, 2**31 - 1))
    
s = Solution()
s.myAtoi("+0 123")
