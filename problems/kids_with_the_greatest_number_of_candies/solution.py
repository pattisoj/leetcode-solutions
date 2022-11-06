class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostCandies = -1
        
        for candy in candies:
            if candy > mostCandies:
                mostCandies = candy
                
        output = []
        
        for candy in candies:
            if candy + extraCandies >= mostCandies:
                output.append(True)
            else:
                output.append(False)
                
        return output