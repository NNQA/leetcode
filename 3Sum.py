


# use hashmap
#  [-1,0,1,2,-1,-4]
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        re = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue


            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum  = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    re.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -=1            

        return re


solution = Solution()
# print(solution.threeSum([-1,0,1,2,-1,-4]))

print(solution.threeSum([0,-4,-1,-4,-2,-3,2]))