class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []

        for i in range(0, len(nums), 2):
            alice = nums[i]
            bob = nums[i+1]
            result.append(bob)
            result.append(alice)

        return result
        