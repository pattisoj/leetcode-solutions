class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (end + begin)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1  
            else:
                begin = mid + 1
        return begin