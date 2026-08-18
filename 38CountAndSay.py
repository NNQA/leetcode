from collections import Counter


class Solution:
    def countAndSay(self, n: int) -> str:

        def group_consecutive_digits(groups: list, s: str):
            previous_digit = s[0]
            count = 0

            for digit in s:
                if digit != previous_digit:
                    groups.append([int(previous_digit), count])
                    previous_digit = digit
                    count = 1
                else:
                    count += 1

            groups.append([int(previous_digit), count])

        def build_next_sequence(groups: list) -> str:
            return "".join(str(count) + str(digit) for digit, count in groups)

        sequence = ""

        for i in range(n):
            groups = []

            if i == 0:
                sequence = "1"
                continue

            group_consecutive_digits(groups, sequence)
            sequence = build_next_sequence(groups)

        return sequence


sol = Solution()
print(sol.countAndSay(5))
