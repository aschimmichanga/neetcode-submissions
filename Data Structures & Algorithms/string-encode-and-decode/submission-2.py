class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return ""
        lengths = ""
        strings = ""
        # write all the string lengths
        for string in strs:
            lengths += str(len(string)) + ","
            strings += string
        return lengths + "#" + strings 
        # separate with #
        # write a joined version of all the strings
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        delim_index = s.find("#")
        
        lengths = [int(x) for x in s[:delim_index - 1].split(",")]


        strings = s[delim_index + 1:]
        decoded = []
        for length in lengths:
            decoded.append(strings[:length])
            strings = strings[length:]
        return decoded