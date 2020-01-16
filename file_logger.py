
class FileLogger:
	__instance = None

	fileLog = False
	file = None;

	def __init__(self, fileLog):
		self.fileLog = fileLog
		if self.fileLog :
			self.file = open("log.txt","w+")

	def __del__(self):
		if self.file is not None:
			self.file.close()

	def log(self, logMessage):
		if self.fileLog:
			self.file.write(logMessage)
