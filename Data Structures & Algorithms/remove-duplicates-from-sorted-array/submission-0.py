class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for num in nums:
            if num in new_list:
                new_list.append(num)
        return new_list