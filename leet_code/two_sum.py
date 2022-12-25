class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		lgth = len(nums)
		for i in range(lgth):
			for j in range(i + 1, lgth):
				if nums[i] + nums[j] == target:
					return (i, j)
		return (-1, -1)

soln = Solution()
tests = (((2, 7, 11, 15), 9), ((3, 2, 4), 6))
for test in tests:
	print(soln.twoSum(test[0], test[1]))
