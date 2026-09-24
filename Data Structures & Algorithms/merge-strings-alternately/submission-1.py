class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = len(word1), len(word2)
        result = []
        i = j = 0
        while i < first or j < second:
            if i < first:
                result.append(word1[i])
            
            if j < second:
                result.append(word2[j])

            i += 1
            j += 1
        return "".join(result)