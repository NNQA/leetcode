class Solution:
    # use hashmap and dictionary
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     seen = {}
    #     for i, val in enumerate(nums):
    #         if val in seen and i - seen[val] <= k:
    #             return True
    #         seen[val] = i
    #     return False
    # use hash set and sliding windows
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, val in enumerate(nums):
            if val in window:
                return True
            window.add(val)
            if len(window) > k:
                window.remove(nums[i - k])

        return False


solution = Solution()
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
# 1 2 3 1
# l
