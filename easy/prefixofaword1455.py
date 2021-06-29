class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if sentence.startswith(searchWord):
            return 1
        i = sentence.find(" "+searchWord)
        if i != -1:
            return sentence.count(" ", 0, i+1)+1

        return -1
