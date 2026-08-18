from collections import Counter

# orginal solution
# class Solution:
#     def countAndSay(self, n: int) -> str:

#         def group_consecutive_digits(groups: list, s: str):
#             previous_digit = s[0]
#             count = 0

#             for digit in s:
#                 if digit != previous_digit:
#                     groups.append([int(previous_digit), count])
#                     previous_digit = digit
#                     count = 1
#                 else:
#                     count += 1

#             groups.append([int(previous_digit), count])

#         def build_next_sequence(groups: list) -> str:
#             return "".join(str(count) + str(digit) for digit, count in groups)

#         sequence = ""

#         for i in range(n):
#             groups = []

#             if i == 0:
#                 sequence = "1"
#                 continue

#             group_consecutive_digits(groups, sequence)
#             sequence = build_next_sequence(groups)

#         return sequence


# optimize solution


class Solution:
    def countAndSay(self, n: int) -> str:
        sequence = "1"

        for _ in range(n - 1):
            result = []
            previous_digit = sequence[0]
            count = 0

            for digit in sequence:
                if digit == previous_digit:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(previous_digit)

                    previous_digit = digit
                    count = 1

            result.append(str(count))
            result.append(previous_digit)

            sequence = "".join(result)

        return sequence


sol = Solution()
print(sol.countAndSay(5))
