import os
import common.path
from logger.logger import Logger
from common.path import getCurrentDirectory
from command.command_executor import run

class Maven:

	logger = None

	debug = False
	projectPath = ""
	module = ""
	client = ""

	def __init__(self, config, module, debug = False):
		self.logger = Logger.getInstance()
		self.debug = debug
		self.projectPath = getCurrentDirectory() + '/'+ module.split('/')[-1]
		self.client = config['client']
		self.module = module
		self.logger.log("Init maven with: " + self.projectPath + " | " + self.module + 
		" | client: " + self.client + 
		" | debug: " +str(self.debug))

	def bumpVersion(self, version):
		self.maven('versions:set -DnewVersion='+ version + ' -DgenerateBackupPoms=false versions:commit')
		
	def maven(self, command):
		fullCommand = self.client + ' ' + command + ' -f ' + self.projectPath
		self.logger.commandLog(fullCommand)
		if not self.debug:
			failure = False
			for partOfOutput in run(fullCommand):
				decodedOutput = str(partOfOutput.decode())
				self.logger.log(decodedOutput)
				if 'BUILD FAILURE' in decodedOutput:
					failure = True
			if failure:
				raise Exception(fullCommand + ' failed')
		
