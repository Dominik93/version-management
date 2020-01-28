from logger.logger import Logger

class Branch:

	logger = None

	master = 'master'
	support = 'support'
	develop = 'develop'

	mainBranch = ''
	developBranch = ''

	def __init__(self, customer, config, version = ''):
		self.logger = Logger.getInstance()
		branchPrefix = customer.lower()
		self.master = config.get('master', self.master)
		self.develop = config.get('develop', self.develop)
		self.support = config.get('support', self.support)
		if version == '':
			if branchPrefix == '':
				self.mainBranch = self.master
				self.developBranch = self.develop
			else:
				self.mainBranch = '/'.join([branchPrefix, self.master])
				self.developBranch = '/'.join([branchPrefix, self.develop])
		else:
			if branchPrefix == '':
				self.mainBranch = self.support + '_' + version
				self.developBranch = self.develop + '_' + version
			else:
				self.mainBranch = '/'.join([branchPrefix, self.support + '_' + version])
				self.developBranch = '/'.join([branchPrefix,  self.develop + '_' + version])
		self.logger.log('Init branch with: ' + str(self.develop) + ' | ' + str(self.master))