class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i-1].lower():
                counter+=1
        return counter