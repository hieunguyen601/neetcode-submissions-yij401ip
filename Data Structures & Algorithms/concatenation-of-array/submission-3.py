class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        res = []
        for num in nums:
            ans.append(num)
        res = ans + nums
        return res