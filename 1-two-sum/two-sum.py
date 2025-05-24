class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums),1):
                if self.nums[i]+self.nums[j] == self.target:
                    return [i,j]
        