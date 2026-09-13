class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # intialize hashmap containing all the maps we will create, with the key as the array, and the value being all the words from that key
        # iterate through the input strs
        # initialize a tuple (arrrays are not hashable) that contains the frequencies of characters for each word as we go through this list
        # So as we keep going we see if the array we just made matches a key we have made in our hashmap, if not, we add this array to the hashmap as a key, along with the corresponding word we are currently at, and if we do, we just add this word to the corresponding key that is already in our hashmap.
        result = []
        mp_frequencies = {}
        for word in strs:
            # initialize an array then convert to tuple containing frequencies
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            if key in mp_frequencies:
                mp_frequencies[key].append(word)
            else:
                mp_frequencies[key] = [word]

        for keyvalue in mp_frequencies.values():
            result.append(keyvalue)

        return result

        

            


        