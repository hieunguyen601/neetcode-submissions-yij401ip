class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter