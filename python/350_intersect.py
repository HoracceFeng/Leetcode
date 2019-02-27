# Given two arrays, write a function to compute their intersection.
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/26/

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

# What if the given array is already sorted? How would you optimize your algorithm?
        ## solution-1
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        index = 0
        res = []
        for i in nums1:
            for j in range(index, len(nums2)):
                if nums2[j] < i:
                    continue
                elif nums2[j] == i:
                    index = j +1
                    res.append(i)
                    break
                else:
                    index = j
                    break
        return res

        # ## solution-2
        # inter = set(nums1) & set(nums2)
        # l = []
        # for i in inter:
        #     l += [i] * min(nums1.count(i), nums2.count(i))  
        # return l

# What if nums1's size is small compared to nums2's size? Which algorithm is better?

# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
