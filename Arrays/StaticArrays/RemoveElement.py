'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

# Problem link: https://leetcode.com/problems/remove-element/description/

# What do I need to do?
'''
1. Filter out all occurrences of "val" from the array "nums".
2. Rearrange the array so the first "k" element does not contain "val", where "k" is the number of elements that remain after removal.
3. Return the value of "k".
'''

# How should I approach this problem?
'''
Understand the problem constraints.
- Can't use extra space for another array to store the result; changes must be done in same array.
'''

# 1. Brute Force | Time Complexity - O(n) | Space Complexity - O(n) 
def removeElement(self, nums: list[int], val: int) -> int:
    tmp = []
    for num in nums:
        if num == val:
            continue
        tmp.append(num)
    for i in range(len(tmp)):
        nums[i] = tmp[i]
    return len(tmp)

# 2. Two Pointers - 1 | Time Complexity - O(n) | Space Complexity - O(1)
def removeElement(self, nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# 3. Two Pointers - 2 | Time Complexity - O(n) | Space Complexity - O(1)
def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            n -= 1
            nums[i] = nums[n]
        else:
            i += 1
    return n