class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        sets=set()
        diff=0
        max_diff=0
        for i in range(len(s)):
            while s[i] in sets:
                sets.remove(s[l])
                l+=1
            diff=i-l+1
            sets.add(s[i])
            max_diff=max(diff,max_diff)


        return max_diff