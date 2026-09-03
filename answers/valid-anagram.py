class Solution:
    def isAnagram(self, word_1: str, word_2: str) -> bool:
        # return sorted(word_1) == sorted(word_2)
        word_1_frequency, word_2_frequency = {}, {}
        if len(word_1_frequency) != len(word_2_frequency): return False
        for letter in word_1:
            if letter in word_1_frequency.keys():
                word_1_frequency[letter] += 1
            else:
                word_1_frequency[letter] = 1
        for letter in word_2:
            if letter in word_2_frequency.keys():
                word_2_frequency[letter] += 1
            else:
                word_2_frequency[letter] = 1
        return word_2_frequency == word_1_frequency