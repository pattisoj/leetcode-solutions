class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while True:
            n = sum([int(a) ** 2 for a in str(n)])
            if n == 1:
                return True
            if n in seen:
                return False
            seen.append(n)