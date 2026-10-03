class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m = {}

        for n in nums1:
            m[n] = m.get(n, 0) + 1
        ans = []
        for n in nums2:
            if n in m:
                ans.append(n)

        return list(set(ans.sort()))
