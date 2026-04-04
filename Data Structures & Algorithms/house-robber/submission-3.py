class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
       
        prev=nums[0]
        curr=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            
            curr,prev=max(prev+nums[i],curr),curr

        return curr