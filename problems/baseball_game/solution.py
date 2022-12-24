class Solution:
    def calPoints(self, operations: List[str]) -> int:
        data = []
        for i in operations:
            try:
                data.append(int(i))
            except:
                if i == "+":
                    data.append(data[len(data) - 1] + data[len(data) - 2])
                elif i == "D":
                    data.append(data[len(data) - 1] * 2)
                elif i == "C":
                    data.pop()
        return sum(data)