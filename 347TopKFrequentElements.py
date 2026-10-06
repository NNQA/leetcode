from collections import Counter
import heapq


class Solution:
    def topKFrequent1(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1:
            return nums
        count = Counter(nums)
        ans = []
        while k > 0:
            prev = 0
            val = 0
            for i, v in count.items():
                if v > prev and i not in ans:
                    prev = v
                    val = i
            ans.append(val)
        return ans

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
