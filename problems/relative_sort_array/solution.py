class Solution:
	def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
		left = []
		for i in arr1:
			if i not in arr2:
				left.append(i)
		left.sort()
		arr2.extend(left)
		arr1.sort(key=lambda x : arr2.index(x))
		return arr1