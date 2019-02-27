# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/25/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        count = 0
        while count+1 <= len(nums)-1:
            if nums[count] == nums[count+1]:
                count += 2
                continue
            else:
                return nums[count]
        return nums[-1]