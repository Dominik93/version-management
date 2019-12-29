from logger import *

class Branch:
	master = ''
	develop = ''

	def __init__(self, customer, version = ''):
		branchPrefix = customer.lower()
		if version == '':
			if branchPrefix == '':
				self.master = 'master'
				self.develop = 'develop'
			else:
				self.master = '/'.join([branchPrefix, 'master'])
				self.develop = '/'.join([branchPrefix, 'develop'])
		else:
			if branchPrefix == '':
				self.master = 'support_' + version
				self.develop = 'develop_' + version
			else:
				self.master = '/'.join([branchPrefix, 'support_' + version])
				self.develop = '/'.join([branchPrefix, 'develop_' + version])
		log('Init branch with: ' + str(self.develop) + ' | ' + str(self.master))