class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        y, x = len(mat), len(mat[0])
        vis, ans = [0] * y, []
        for j in range(x+1):
            for i in range(y):
                if not vis[i] and (j == x or not mat[i][j]):
                    ans.append(i)
                    vis[i] = 1
                if len(ans) == k: return ans