from collections import Counter


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                break
        return sum(count.values())
