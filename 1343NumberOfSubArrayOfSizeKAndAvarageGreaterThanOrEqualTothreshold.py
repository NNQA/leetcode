class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0
        cur_sum = 0
        count = 0
        for r in range(len(arr)):
            cur_sum += arr[r]
            if r - l + 1 == k:
                if cur_sum >= k * threshold:
                    count += 1
                cur_sum -= arr[l]
                l += 1
            if r - l + 1 > k:
                cur_sum -= arr[r]
                l += 1
        return count


sol = Solution()
print(sol.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
