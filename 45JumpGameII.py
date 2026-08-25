class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                jumps += 1
                break

            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


solution = Solution()
print(solution.jump([1, 2, 1, 1, 1]))
