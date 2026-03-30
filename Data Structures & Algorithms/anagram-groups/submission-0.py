from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        val=defaultdict(list)

        for s in strs:
            counter=[0]*26
            for i in s:
                counter[ord(i)-ord('a')]+=1
            full = tuple(counter)
            val[full].append(s)

        return list(val.values())
        