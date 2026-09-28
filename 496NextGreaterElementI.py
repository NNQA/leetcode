class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        map2 = {}
        for i in range(len(nums2) - 1):
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i] and nums2[i] not in map2:
                    map2[nums2[i]] = nums2[j]
                    break

        res = []
        for num in nums1:
            if num in map2:
                res.append(map2[num])
            else:
                res.append(-1)
        return res

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[x] for x in nums1]


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
