

class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_abs_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        return [  
            (arr[i], arr[i + 1])
            for i in range(len(arr) -1)
            if abs(arr[i + 1] - arr[i]) == min_abs_diff 
        ]
    

solution = Solution()
print(solution.minimumAbsDifference([40,11,26,27,-20]))