

class Solution:
    def numberOfStableArrays(self, zero, one, limit):

        MOD = 10**9 + 7
        memo ={}

        def solve(one_left, zero_left, left_was_one):
            if one_left == 0 and zero_left == 0:
                return 1
            
            state = (one_left, zero_left, left_was_one)

            if(state in memo):
                return memo[state];
            result = 0
            if left_was_one:
                for i in range(1, min(zero_left, limit) + 1):
                    result = (result + solve(one_left, zero_left - i, 0)) % MOD
            else:
                for i in range(1, min(one_left, limit) + 1):
                    result = (result + solve(one_left - i, zero_left, 1)) % MOD

            memo[state] = result
            return memo[state]  
        return (solve(one, zero, 1) + solve(one, zero, 0)) % MOD

solution = Solution()
print(solution.numberOfStableArrays(1, 2, 1))