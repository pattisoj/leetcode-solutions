class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        
        if n % 2 != 0: ans.append(0)
        
        digits = n // 2
        
        for i in range(1, digits+1):
            ans.append(i)
            ans.append(-1*i)
        
        return ans