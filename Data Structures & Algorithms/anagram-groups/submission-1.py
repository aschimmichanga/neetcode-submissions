class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroupings = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            anagramGroupings[sortedString].append(string)

        return list(anagramGroupings.values())

