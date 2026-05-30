"""
LeetCode 1. Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

=== Problem ===
Given an array nums and a target, return indices of two numbers that add up to target.
Each input has exactly one solution. Can't use the same element twice.

=== Thought Process ===
1. First idea: brute force, try every pair with two loops
2. For each num, the number I need is: target - num
3. Instead of using inner loop to find it (O(n)), use a dict to look it up (O(1))
4. Key insight: traverse once, check dict first, then store current num

=== Mistakes & Lessons ===
- Used same variable name (num) in both loops -> inner overwrites outer. Use different names!
- Wrote `if:` without a condition -> syntax error. `if` always needs a condition after it
- Confused = (assignment) with == (comparison) in if statement
- Used print() instead of return -> LeetCode needs return
- Forgot to store num into hashmap -> dict stays empty, never finds anything
- Returned (i, i1) tuple instead of [i, i1] list -> works but not strictly correct

Key takeaway: dict lookup replaces inner loop. Store AFTER checking to avoid self-match.

=== Complexity ===
Brute Force: Time O(n^2) | Space O(1)
Optimized:   Time O(n)   | Space O(n)

=== Related Problems ===
- 15. 3Sum
- 167. Two Sum II (sorted array)
"""

from typing import List


# ---- Brute Force ---- Beats 5.63% (2747ms)
class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            tnum = target - num
            for i1, num1 in enumerate(nums):
                if i1 != i and num1 == tnum:
                    return [i, i1]


# ---- Optimized (Hash Map) ----
class OptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}                        # create empty dict (the "register")
        for i, num in enumerate(nums):      # loop with index and value
            tnum = target - num             # the number I need
            if tnum in hashmap:             # check: is it registered?
                return [hashmap[tnum], i]   # found! return both indices
            hashmap[num] = i                # not found, register myself
