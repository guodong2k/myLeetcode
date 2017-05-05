class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num=sorted(nums1+nums2)
        long=len(num)
        if long%2==0:
            n1=num[long/2-1:long/2]
            n2=num[long/2:long/2+1]
            median=float(n1[0]+n2[0])/2
        else:
            n=num[(long-1)/2:(long-1)/2+1]
            median = n[0]
        return median
