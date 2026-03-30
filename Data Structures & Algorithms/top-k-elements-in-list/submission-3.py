from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq=[[] for i in range(len(nums)+1)]
        count={}

        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1

        for n,c in count.items():
            freq[c].append(n)

        res=[]

        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                k-=1

                if k ==0:
                    return res

