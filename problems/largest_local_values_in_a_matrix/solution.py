class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[0 for i in range(n-2)] for j in range(n-2)]
        for k in range(n-2):
            for h in range(n-2):
                maxi=-float('inf')
                for i in range(k,k+3):
                    for j in range(h,h+3):
                        if grid[i][j]>maxi:
                            maxi=grid[i][j]
                ans[k][h]=maxi
        return ans