class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        li =[int(d) for d in str(num)]
        summ =sum(li)
        if summ<10:
            return summ
        else:
            return (self.addDigits(summ))

            
        