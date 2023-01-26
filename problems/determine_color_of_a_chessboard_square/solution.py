class Solution:
    def squareIsWhite(self, c: str) -> bool:
        # This orders the alphabet like a=1, b=2, c=3...
        order=ord(c[0])-96 
        
        if order%2==1 and int(c[1])%2==1: 
            return False
        if order%2==0 and int(c[1])%2==0: 
            return False
        return True 