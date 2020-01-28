import sys
import os
from logger.logger import Logger

class Cleaner:

	logger = None

	system = 'windows'

	def __init__(self, system):
		self.logger = Logger.getInstance()
		self.system = system
		self.logger.log("Init cleaner with " + self.system)

	def clean(self, directory):
		if self.system == 'windows':
			os.system('rd /s /q "' + directory + '"')
		else:
			os.system('rm -r -f ' + directory)
