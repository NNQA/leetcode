class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        ones_count = 0
        left = 0

        for right in range(len(s)):
            if s[right] == "1":
                ones_count += 1
            print("right", right, ones_count)
            while ones_count == k:
                sub = s[left : right + 1]
                print("right", right, ones_count, sub)
                if (
                    not ans
                    or len(sub) < len(ans)
                    or (len(sub) == len(ans) and sub < ans)
                ):
                    ans = sub

                if s[left] == "1":
                    ones_count -= 1
                left += 1

        return ans


solution = Solution()
print(solution.shortestBeautifulSubstring("100011001", 3))
# print(solution.shortestBeautifulSubstring("000", 3))
