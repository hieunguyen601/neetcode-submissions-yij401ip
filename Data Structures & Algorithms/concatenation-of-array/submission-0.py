class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = nums.copy()
        for element in new_list:
            nums.append(element)
        return nums