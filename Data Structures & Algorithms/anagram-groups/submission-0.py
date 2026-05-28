class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        hashIndex = 0
        anagramHash = dict()
        anagramGroupings = []

        for stringIndex, string in enumerate(strs):
            sortedString = "".join(sorted(string))
            if stringIndex == 0:
                anagramGroupings.append([string])
                anagramHash[sortedString] = hashIndex
                hashIndex += 1
            else:
                if sortedString in anagramHash:
                    anagramGroupings[anagramHash[sortedString]].append(string)
                else:
                    anagramGroupings.append([string])
                    anagramHash[sortedString] = hashIndex
                    hashIndex += 1

        return anagramGroupings

