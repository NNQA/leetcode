class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        ans = 0
        for w in words:
            for c in w:
                if c not in allowed:
                    break
            else:
                ans += 1
        return ans


print(Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
