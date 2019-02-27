# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/28/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        nums.reverse()
        while count < len(nums):
            if nums[count] == 0:
                nums.insert(0, nums.pop(count))
                count += 1
            else:
                count += 1
                continue
        nums.reverse()            
            