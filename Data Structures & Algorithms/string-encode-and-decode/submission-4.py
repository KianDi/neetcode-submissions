class Solution:

    def encode(self, strs: List[str]) -> str:
        ### input: takes in a list of strings
        ### outputs: a string
        ### chars could be any character
        encoded_word = ""
        for string in strs:
            encoded_word += str(len(string)) + "#" + string
        return encoded_word


    def decode(self, s: str) -> List[str]:
        ### input: takes in a string, 
        ### outputs: a list of strings
        result = []
        i = 0
        while i < len(s):
            ## we have to take in the number before the marker
            ## we do this using a while loop, tracking j and i
            ## once we find it we know the number is from the 
            #indices from i to until j
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 +length])
            i = j + 1 + length
        return result
                