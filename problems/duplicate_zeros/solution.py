class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        q = []
        if arr:
            for index in range(len(arr)):                
                if arr[index] == 0:
                    q.append(0)                                                            
                if q: 
                    q.append(arr[index])
                    arr[index] = q.pop(0)
        