"""
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations."""

from math import ceil as UpperValue
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = nums[0]
        n = len(nums)
        i = 1
        ans = 0
        while n - i:
            tillNow = UpperValue(tot/i)
            tot += nums[i]
            i += 1
            current = UpperValue(tot/i)
            ans = max(tillNow, current, ans)
        return ans
