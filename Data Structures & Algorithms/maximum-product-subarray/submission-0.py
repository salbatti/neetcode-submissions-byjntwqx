class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=1
        curr_min=1
        glb_max=nums[0]

        for i in range(len(nums)):
            tmp=curr_max
            curr_max=max(nums[i],nums[i]*curr_max,nums[i]*curr_min)
            curr_min=min(nums[i],nums[i]*tmp,nums[i]*curr_min)
            glb_max=max(curr_max,glb_max)

        return glb_max