class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set(list(sentence))
        return True if len(sentence) == 26 else False