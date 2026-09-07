class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = defaultdict(list)
        for element in strs:
            new_dict[''.join(sorted(element))].append(element)
        return list(new_dict.values())
        