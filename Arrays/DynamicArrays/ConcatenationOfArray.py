'''
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
'''

# Problem Link: https://leetcode.com/problems/concatenation-of-array/description/

# 1. Iteration (Two Pass) | Time Complexity - O(n) | Space Complexity O(1)
def getConcatenation(self, nums: List[int]) -> List[int]:
    ans = []
    for i in range(2):
        for num in nums:
            ans.append(num)
    return ans

#2. Iteration (One Pass) | Time Complexity - O(n) | Space Complexity O(1)
def getConcatenation(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans