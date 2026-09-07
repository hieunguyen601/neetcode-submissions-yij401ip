class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        array = []
        
        for num, value in count.items():
            array.append([value,num])
        array.sort()

        result = []
        while len(result) < k:
            result.append(array.pop()[1])
        return result
            