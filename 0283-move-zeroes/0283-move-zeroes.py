class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        prev_indx = 0
        for i in range(0,len(nums)):
            if nums[i] !=0:
                hold =nums[prev_indx]
                nums[prev_indx] = nums[i]
                nums[i] = hold
                prev_indx+=1
