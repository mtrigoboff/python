class Solution(object):
	def __init__(self):
		self.digit_vals = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
		self.digit_pairs = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}

	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		val = 0
		i = 0
		while i < len(s) - 1:
			try:
				val += self.digit_pairs[s[i:i + 2]]
				i += 2
			except KeyError:
				val += self.digit_vals[s[i]]
				i += 1
		if i < len(s):
			val += self.digit_vals[s[i]]
		return val

soln = Solution()
tests = ('III', 'IV', 'I', 'V', 'LVIII', 'MCMXCIV', 'IVX', 'XIV')
for test in tests:
	print(f'{test}: {soln.romanToInt(test)}')
