class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        val=set()
        diff=0
        max_val=0
        for i in range(len(s)):
            while s[i] in val:
                val.remove(s[l])
                l+=1
            val.add(s[i])
            diff=i-l+1
            max_val=max(diff,max_val)

        return max_val