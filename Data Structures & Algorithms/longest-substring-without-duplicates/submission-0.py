class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newSet = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in newSet:
                newSet.remove(s[left])
                left += 1
            newSet.add(s[right])
            result = max(result, right - left + 1)
        return result