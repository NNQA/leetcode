class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        l = 0
        ans = 0
        map_s = {}
        for r in range(len(s)):

            if s[r] in map_s:
                l = max(map_s[s[r]] + 1, l)
            map_s[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("1R1T7"))
