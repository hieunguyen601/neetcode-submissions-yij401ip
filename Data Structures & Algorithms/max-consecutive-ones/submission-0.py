class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_num = 0
        for i in range(len(nums)):
             if nums[i] == 1 and nums[i] == 0:
                consecutive_num += 1;
        return consecutive_num