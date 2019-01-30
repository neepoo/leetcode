class Solution(object):
    def detectCapitalUse(self, word):
        c = 0
        for i in word:
            if i == i.upper():
                c += 1
        return c == len(word) or (c == 1 and word[0] == word[0].upper()) or c == 0 
