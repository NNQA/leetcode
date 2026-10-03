from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        count = Counter()
        for word in words:
            count.update(word)

        n = len(words)
        return all(v % n == 0 for v in count.values())


print(Solution().makeEqual(["abc", "a", "bc"]))  # Output: True
