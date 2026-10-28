class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newList = defaultdict(list)
        for element in strs:
            sorted_element = sorted(element)
            newList["".join(sorted_element)].append(element)
        return list(newList.values())