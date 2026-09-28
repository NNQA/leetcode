from collections import defaultdict


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:

        mapS = defaultdict(int)

        for char in arr:
            mapS[char] += 1
        print(mapS)
        for index, (key, value) in enumerate(mapS.items()):
            if value == 1:
                k -= 1
            if k == 0:
                return key
            print(key, value)
        return ""


print(Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
