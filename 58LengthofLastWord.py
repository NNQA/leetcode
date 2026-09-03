class Solution:
    # built-in functions
    def lengthOfLastWordBuilt_In(self, s: str) -> int:
        return s.capitalize().split()[-1]

    # normal ways
    def lengthOfLastWord(self, s: str) -> int:

        check_blank = True
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                check_blank = False
                count += 1
            elif check_blank == False and s[i] == " ":
                break
        return count


solution = Solution()
print(solution.lengthOfLastWord("Hello World   "))
