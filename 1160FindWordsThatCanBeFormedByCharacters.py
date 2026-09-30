from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0

        for w in words:
            wc = Counter(w)
            if all(cnt[c] >= v for c, v in wc.items()):
                ans += len(wc)
        return ans


print(Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach"))
