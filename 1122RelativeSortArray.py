class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        mapA2 = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: mapA2.get(x, len(arr2) + x))
