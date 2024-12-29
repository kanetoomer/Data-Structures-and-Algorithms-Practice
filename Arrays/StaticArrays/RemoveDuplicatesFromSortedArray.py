'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

'''

# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# What do I need to do?
'''
Take an array and remove duplicates. Convert them into a new array where the duplicates are removed.
'''

# How should I approach this problem?
'''
Understand the problem constraints.
- "nums" is sorted into "non-decreasing" order.
- Need to modify the array array in-place to include only unique elements up "k" positions.
- Goal is to minimize the extra space (ideally O(1))
'''

# Solution Options:

# 1. Sorted Set | Time Complexity - O(nlogn) | Space Complexity O(n)
def removeDuplicates(self, nums: list[int]) -> int:
    unique = sorted(set(nums))
    nums[:len(unique)] = unique
    return len(unique)

# 2. Two Pointers - 1 | Time Complexity O(n) | Space Complexity O(1)
def removeDuplicates(self, nums: list[int]) -> int:
    n = len(nums)
    l = r = 0
    while r < n:
        nums[l] = nums[r]
        while r < n and nums[r] == nums[l]:
            r += 1
        l += 1
    return l

# 3. Two Pointers - 2 | Time Complexity O(n) | Space Complexity O(1)
def removeDuplicates(self, nums: list[int]) -> int:
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l