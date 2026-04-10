class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for first in s:
            countS.append(first)
        
        for second in t:
            countT.append(second)

        if countS.has(counT):
            return True