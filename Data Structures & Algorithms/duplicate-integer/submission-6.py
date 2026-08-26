class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = Counter(nums)
        for num in nums:
            if new_nums[num] >= 2:
                return True
        return False