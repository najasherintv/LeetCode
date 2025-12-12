class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = sum(nums)
        digit_sum = 0

        for n in nums:
            for digit in str(n):
                 digit_sum += int(digit)
        return (element_sum - digit_sum)         
        