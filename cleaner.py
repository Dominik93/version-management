import sys
import os

class Cleaner:
	system = 'windows'

	def __init__(self, system):
		self.system = system
		print("Init cleaner with " + self.system)

	def clean(self, directory):
		if self.system == 'windows':
			os.system('rd /s /q "' + directory + '"')
		else:
			os.system('rm -r -f ' + directory)
