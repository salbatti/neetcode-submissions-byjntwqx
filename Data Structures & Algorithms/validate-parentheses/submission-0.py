class Solution:
    def isValid(self, s: str) -> bool:
        mapping={']':'[','}':'{',')':'('}

        stk=[]
        for i in s:
            if i in mapping.values():
                stk.append(i)
            elif not stk or mapping[i] != stk.pop():
                return False

        return len(stk)==0
        