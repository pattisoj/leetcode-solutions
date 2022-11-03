class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineLetters = {}
        
        for keys in magazine:
            magazineLetters[keys] = magazineLetters.get(keys, 0) + 1
        
        for keys in ransomNote:
            magazineLetters[keys] = magazineLetters.get(keys, 0) - 1
            if magazineLetters[keys] <0:
                return False
    
        
        return True
        