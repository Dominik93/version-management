
class SimpleLogger:

	def log(self, logMessage):
		newLine = ''
		if not logMessage.endswith('\n'):
			newLine = '\n'
		print(logMessage, end = newLine)