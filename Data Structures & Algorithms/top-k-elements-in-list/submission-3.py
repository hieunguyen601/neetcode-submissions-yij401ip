class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for value, freq in count.items():
            arr.append([freq, value])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[-1])
        return result