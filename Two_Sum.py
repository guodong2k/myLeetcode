class Solution(object):
    def twoSum(self, nums, target):
        i=0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if nums[i]+ nums[j]==target and i!=j:
                    return [i,j]
                else:
                    j=j+1
            i=i+1