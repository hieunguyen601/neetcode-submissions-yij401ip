class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = set()
        for num in nums:
            if num in new_array:
                return True
            new_array.add(num)
        return False