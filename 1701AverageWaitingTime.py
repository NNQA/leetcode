class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        time = 0
        wait = 0
        for arrival, duration in customers:
            time = max(time, arrival) + duration
            wait += time - arrival

        return wait / len(customers)
