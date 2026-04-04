class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def func1(nums):
            if len(nums)==1:
                return nums[0]

            prev=nums[0]
            curr=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                tmp=curr
                curr=max(prev+nums[i],curr)
                prev=tmp

            return curr

        return max(func1(nums[:len(nums)-1]),func1(nums[1:]))