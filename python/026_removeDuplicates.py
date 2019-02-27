## 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
## 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
## https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/21/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

## solution-1
        count = 0
        while count+1 <= len(nums)-1:
            if nums[count] == nums[count+1]:
                nums.pop(count+1)
            else:
                count += 1
        return len(nums)

## solution-2
        for i in range(len(nums)):
            for _ in range(i+1, len(nums)):
                if nums[i] == nums[i+1]:
                    del nums[i+1]
                else:
                    break
        return len(nums)
