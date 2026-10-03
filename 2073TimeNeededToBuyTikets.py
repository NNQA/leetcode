class Solution:
    # def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:

    #     count = 0
    #     i = 0
    #     n = len(tickets)
    #     while tickets[k] > 0:
    #         if tickets[i % n] != 0:
    #             count += 1
    #         tickets[i] -= 1
    #         i += 1
    #     return count
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
                print(i, tickets[i], tickets[k], time)
            else:
                time += min(tickets[i], tickets[k] - 1)
        return time


Solution().timeRequiredToBuy([2, 3, 2], 2)
