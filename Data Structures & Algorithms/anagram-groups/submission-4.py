class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for element in strs:
            sortedElement = ''.join(sorted(element))
            output[sortedElement].append(element)
        return list(output.values())