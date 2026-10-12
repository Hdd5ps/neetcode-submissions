class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths don't match, they cannot be anagrams
        if len(s) != len(t):
            return False

        # creating two hashmaps
        countS, countT = {}, {}

        # Correctly iterate through the characters of both strings
        for char in s:
            countS[char] = 1 + countS.get(char, 0)
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # Compare character frequencies safely
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
