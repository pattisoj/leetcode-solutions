class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        return min(dic, key = dic.get)