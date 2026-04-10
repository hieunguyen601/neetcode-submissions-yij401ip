class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for element in nums:
            new_list.append(element)
        return new_list