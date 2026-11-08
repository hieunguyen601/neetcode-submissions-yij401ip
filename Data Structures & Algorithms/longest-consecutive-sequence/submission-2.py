class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        longest = 0
        for num in newSet:
            if (num - 1) not in newSet:
                length = 0
                while (num + length) in newSet:
                    length += 1
                longest = max(longest, length)
        return longest