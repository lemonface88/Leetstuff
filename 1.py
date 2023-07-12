class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)-1):

            for c in range(i+1, len(nums)):
                
                if (nums[i]+ nums[c]) == target:
                    return([i, c])