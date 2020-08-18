from logger.logger import Logger

class Branch:

	logger = None

	mainBranch = ''

	def __init__(self, config):
		self.logger = Logger.getInstance()
		self.mainBranch = config.get('mainBranch')
		self.logger.log('Init branch with: ' + str(self.mainBranch))