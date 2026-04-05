class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amt=[amount+1]*(amount+1)
        amt[0]=0
        for i in range(amount+1):
            for c in coins:
                if i-c>=0:
                    amt[i]=min(amt[i],1+amt[i-c])

        if amt[-1]!=amount+1:
            return amt[-1]
        else:
            return -1