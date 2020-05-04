from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_counts = Counter(magazine)
        for word in ransomNote:
            if word_counts[word] > 0:
                word_counts[word] -= 1
            else:
                return False
        return True
