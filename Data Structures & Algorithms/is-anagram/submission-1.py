class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) !=len(t):
            return False
        hashset={}

        for i in s:
            if i not in hashset:
                hashset[i]=1
            else:
                hashset[i]+=1

        for i in t:
            if i not in hashset or hashset[i]==0:
                return False
            
            hashset[i]-=1

        return True