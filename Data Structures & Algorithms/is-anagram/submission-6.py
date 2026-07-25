class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            characterS = s[i]
            characterT = t[i]
            if characterS in countS:
                countS[characterS] += 1
            else:
                countS[characterS] = 1
            
            if characterT in countT:
                countT[characterT] += 1
            else:
                countT[characterT] = 1
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True