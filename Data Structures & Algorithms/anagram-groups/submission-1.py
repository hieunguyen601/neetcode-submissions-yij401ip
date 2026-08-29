class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = defaultdict(list)
        for element in strs:
            sortedString = ''.join(sorted(element))
            new_dict[sortedString].append(element)
        return list(new_dict.values())