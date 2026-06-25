
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     char_set = set()
    #     max_length = 0
    #     for i in range(len(s)):
    #         j = i
    #         while s[j] not in char_set:
    #             char_set.add(s[j])
    #             j += 1
    #             if j == len(s):
    #                 break
    #         max_length = max(max_length, len(char_set))
    #         char_set.clear()
    #     return max_length
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_len = 0 
        start = 0
        for end in range(len(s)):
            if s[end] in char_dict:
                start = max(start, char_dict[s[end]] + 1)
            char_dict[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len
solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))  # Output: 3