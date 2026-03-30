from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)
        for s in strs:
            counter=[0]*26
            for i in s:
                counter[ord(i)-ord('a')]+=1
            mer=tuple(counter)
            res[mer].append(s)

        return list(res.values())
        