class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        for char in s:
            mp1[char] = 1 + mp1.get(char, 0)
        for char in t:
            mp2[char] = 1 + mp2.get(char, 0)
        return mp1 == mp2
        