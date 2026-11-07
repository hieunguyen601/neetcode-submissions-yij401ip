class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_nums = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in previous_nums:
                return [previous_nums[complement], index]
            previous_nums[num] = index
        return []