class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        min_v=nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                min_v=min(min_v,nums[l])
                return min_v

            m=(l+r)//2

            min_v=min(min_v,nums[m])

            if nums[m]>=nums[l]:
                l=m+1
            elif nums[m]<nums[l]:
                r=m-1

        return min_v