
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         results = []
#         nums.sort()

#         for i in xrange(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             l, r = i + 1, len(nums)-1
#             while l < r:
#                 total = nums[i] + nums[l] + nums[r]
#                 if total < 0:
#                     l += 1
#                 elif total > 0:
#                     r -= 1
#                 else:
#                     results.append([nums[i], nums[l], nums[r]])
#                     while l < r and nums[l] == nums[l+1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r-1]:
#                         r -= 1
#                     l += 1; r -= 1
#         return results
a = []
a.append((1,2,3))
print a