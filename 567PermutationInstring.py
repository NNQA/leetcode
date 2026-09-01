class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:

    #     table = {}
    #     n = len(s1)
    #     l = 0
    #     for c in s1:
    #         table[c] = table.get(c, 0) + 1
    #     print(table)
    #     for r in range(len(s2)):
    #         if s2[r] in table:
    #             table[s2[r]] -= 1
    #             while table[s2[r]] < 0:
    #                 table[s2[l]] += 1
    #                 l += 1
    #             if r - l + 1 == n:
    #                 return True
    #         else:
    #             while l < r:
    #                 table[s2[l]] += 1
    #                 l += 1
    #             l += 1
    #     return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        l = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0
        print(matches)
        print(s1_count)
        print(s2_count)
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[l]) - ord("a")
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
            l += 1
            index = ord(s2[r]) - ord("a")
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
            print("s1", s1_count)
            print("s2", s2_count)
        return matches == 26


# "ooolleoooleh"
# "hello"

# "ooolleooolleh"
solution = Solution()
print(solution.checkInclusion("ab", "aidbaooo"))
