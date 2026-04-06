class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def func1(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return

            if i==len(nums) or total > target:
                return

            curr.append(nums[i])
            func1(i,curr,total+nums[i])
            curr.pop()
            func1(i+1,curr,total)



        func1(0,[],0)

        return res