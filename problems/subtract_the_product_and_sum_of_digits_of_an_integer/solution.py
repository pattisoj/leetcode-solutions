class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		if n == 0:
			return 0

		product = 1
		add = 0
		for i in str(n):
			product *= int(i)
			add += int(i)
		return product - add