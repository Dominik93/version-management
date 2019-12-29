
class Input:
	silent = False

	def __init__(self, silent):
		self.silent = silent
		print("Init input with " + str(self.silent))

	def askAndAnswer(self, object, question):
		if object is None:
			return input(question)
		return object

	def ask(self, question):
		if not self.silent:
			answer = input(question)
			if not (answer.upper() == "Y" or answer.upper() == 'YES'):
				raise Exception('Process was interrupted by user. ' + question + ': ' + answer)
