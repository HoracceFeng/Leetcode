# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/24/


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
## solution-1: TimeOut
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                else:
                    continue
        return False
        
## solution-2: 
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                continue
            else:
                return True
        return False