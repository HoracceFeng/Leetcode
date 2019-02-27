# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/29/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
## solution-1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] != target:
        #             continue
        #         else:
        #             return [i,j]
        
## solution-2
        # sortId = sorted(range(len(nums)), key= lambda k:nums[k])
        # head = 0
        # tail = len(nums)-1
        # sum = nums[sortId[head]] + nums[sortId[tail]]
        # while sum != target:
        #     if sum < target:
        #         head += 1
        #     else:
        #         tail -= 1
        #     sum = nums[sortId[head]] + nums[sortId[tail]]
        # return [sortId[head], sortId[tail]]

## solution-3
        d = dict()
        for index, i in enumerate(nums):
            tmp = target - i
            if tmp in d:
                return [index, d[tmp]]
            d[i]=index