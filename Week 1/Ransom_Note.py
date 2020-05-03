class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in magazine:
            if i in ransomNote:
                magazine.remove(i)
            else:
                return False
        return True
        
