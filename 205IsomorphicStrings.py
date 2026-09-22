class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        indexS = [0] * 200
        indexT = [0] * 200
        for i in range(len(s)):
            if indexS[ord(s[i])] != indexT[ord(t[i])]:
                return False
            indexT[ord(t[i])] = i + 1
            indexS[ord(s[i])] = i + 1

        return True


print(Solution().isIsomorphic("badc", "baba"))
