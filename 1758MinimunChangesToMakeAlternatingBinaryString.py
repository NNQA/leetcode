class Solution:
    def minOperations1(self, s: str) -> int:

        cur = cnt1 = 0
        for c in s:
            if int(c) != cur:
                cnt1 += 1
            cur ^= 1

        cnt2 = 2
        cur = 1

        for c in s:
            if int(c) != cur:
                cnt2 += 1
            cur ^= 1
        return min(cnt1, cnt2)

    def minOperations(self, s: str) -> int:
        cnt = sum(c != "01"[i & 1] for i, c in enumerate(s))
        return min(cnt, len(s) - cnt)


print(Solution().minOperations("1111"))
