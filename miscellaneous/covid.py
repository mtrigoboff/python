class Patient():
	def __init__(self, name, age, temp, o2sat, cough):
		self.name = name
		self.age = age
		self.temp = temp
		self.o2sat = o2sat
		self.cough = cough
		self.score = 0
	
	def __str__(self):
		nameColon = self.name + ':'
		return f'{nameColon:10} age: {self.age:3}, temp: {self.temp:3}, o2Sat: {self.o2sat:4.2}, cough: {str(self.cough):5} -> score: {int(self.score):3}'

class Rule():
	def __init__(self, cond, op, trueVal, falseVal):
		self.cond = cond
		self.op = op
		self.trueVal = trueVal
		self.falseVal = falseVal

	def evaluate(self, patient):
		cond = 'patient.' + self.cond
		effect = 'patient.score ' + self.op + '= '
		if eval(cond):
			effect += str(self.trueVal)
		else:
			effect += str(self.falseVal)
		exec(effect)

rules = (Rule('temp > 101', '+', 3, 0),
		 Rule('o2sat < 0.94', '+', 5, 0),
		 Rule('cough == True', '+', 4, 0),
		 Rule('age <= 20', '*', 0.8, 1),
		 Rule('age > 65', '*', 1.5, 1))

patients = (Patient('Bob', 70, 103, 0.87, True),
			Patient('Mary', 30, 98, 0.95, True),
			Patient('Henry', 12, 97, 0.99, False))

def run():
	for patient in patients:
		for rule in rules:
			rule.evaluate(patient)
		print(patient)

run()