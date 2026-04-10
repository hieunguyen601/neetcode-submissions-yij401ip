class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []
        first_num = nums[0]
        for i in range(len(nums)):
            if nums[i] != first_num:
                first_num = nums[i]
                result.append(first_num)
                return True
            else:
                return False