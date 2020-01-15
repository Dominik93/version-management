
class Logger:
	__instance = None
	fileLog = False
	file = None;

	@staticmethod
	def getInstance():
		return Logger.__instance

	@staticmethod
	def initialize(fileLog):
		if Logger.__instance == None:
			Logger(fileLog)
		return Logger.__instance

	def __init__(self, fileLog):
		if Logger.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			self.fileLog = fileLog
			if self.fileLog :
				self.file = open("log.txt","w+")
			Logger.__instance = self

	def __del__(self):
		if self.file is not None:
			self.file.close()

	def log(self, logMessage):
		print(logMessage)
		if self.fileLog:
			self.file.write(logMessage+'\n')


	def specialLog(self, logMessage):
		print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
		print(logMessage)
		print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
		if self.fileLog:
			self.file.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'+'\n')
			self.file.write(logMessage+'\n')
			self.file.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'+'\n')


	def commandLog(self, logMessage):
		print('>>>>>>>>>>     ' + logMessage+'\n')
		if self.fileLog:
			self.file.write(logMessage+'\n')

	def prettyLog(self, logMessage):
		print('------------------------------------------------------------------------------------')
		print(logMessage)
		print('------------------------------------------------------------------------------------')
		if self.fileLog:
			self.file.write('------------------------------------------------------------------------------------'+'\n')
			self.file.write(logMessage+'\n')
			self.file.write('------------------------------------------------------------------------------------'+'\n')