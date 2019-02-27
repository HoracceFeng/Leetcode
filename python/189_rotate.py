# Given an array, rotate the array to the right by k steps, where k is non-negative.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/23/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
## solution-1
        for i in range(k % len(nums)):
            nums.insert(0, nums.pop())

    
## solution-2
        # for i in range(len(nums) - k % len(nums)):
        #     nums.append(nums.pop(0))
        

        