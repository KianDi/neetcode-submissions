class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssort = sorted(s)
        rsort = sorted(t)
        if ssort != rsort:
            return False
        return True
        