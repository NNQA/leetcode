"""Solution for: Given an integer array nums, return True if any value
appears at least twice in the array, and return False if every element is
distinct.

This file provides:
- containsDuplicate(nums): O(n) time, O(n) extra space using a set.
- a small built-in test harness that runs a few cases when executed.
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """Return True if any value appears at least twice in nums.

    Time: O(n) — iterate once.
    Space: O(n) — store seen values in a set.
    """
    seen = set()
    for v in nums:
        if v in seen:
            return True
        seen.add(v)
    return False


def _run_tests() -> int:
    cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([], False),
        ([0, 0], True),
        ([2], False),
        (list(range(1000)), False),
        (list(range(500)) + list(range(500)), True),
    ]

    all_passed = True
    for i, (nums, expected) in enumerate(cases, start=1):
        got = contains_duplicate(nums)
        ok = got == expected
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} — got {got}, expected {expected}")
        if not ok:
            all_passed = False

    return 0 if all_passed else 1


if __name__ == "__main__":
    # Run built-in tests when executed directly
    raise SystemExit(_run_tests())
