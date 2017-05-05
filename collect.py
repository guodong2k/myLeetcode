#263. Ugly Number
# -*- coding: utf-8 -*-
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False
        while num!=1:
            if num%2==0:
                num=num / 2
                continue
            elif num%3==0:
                num = num / 3
                continue
            elif num%5==0:
                num = num / 5
                continue
            else:
                return False
        return True

#263. Ugly Number 2
# -*- coding: utf-8 -*-
class Solution:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5=q[i2]*2, q[i3]*3, q[i5]*5
            m = min(m2,m3,m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += m,
        return q[-1]
        

#414. Third Maximum Number    
# -*- coding: utf-8 -*-
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ids = list(set(nums))

        if len(ids)<3:
            ids.sort()
            return ids[-1]
        else:
            ids.sort(reverse=True)
            return ids[2]

            

