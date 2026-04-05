class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res=[1]*n
        for i in range(m-1):
            res1=[1]*n
            for j in range(n-2,-1,-1):
                res1[j]=res[j]+res1[j+1]
            res=res1

        return res[0]