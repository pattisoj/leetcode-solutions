class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sum1 = 0
        for x in  sentences:
            count = 1
            for i in x:
                if i == " ":
                    count +=1
            sum1 = max(sum1, count)
        return sum1