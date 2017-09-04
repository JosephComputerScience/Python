"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        hashm = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashm:
                result = [hashm[compliment], i]
                break
            elif not nums[i] in hashm:
                hashm[nums[i]] = i
            
        return result
        