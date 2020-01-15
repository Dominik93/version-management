import os
from logger import *
from path import *

class Git:

	logger = None

	debug = False
	projectPath = ""
	module = ""
	url = ""
	client = ""

	def __init__(self, config, module, debug = False):
		self.logger = Logger.getInstance()
		self.debug = debug
		self.projectPath = getCurrentDirectory() + '/'+ module.split('/')[-1]
		self.module = module
		self.url = config['GIT']['url']
		self.client = config['GIT']['client']
		self.logger.log("Init git with: " + self.projectPath + " | "+  self.url + " | " + self.module + " | client: " + self.client + " | debug: " + str(self.debug))

	def clone(self):
		self.logger.commandLog('git clone '+ self.url + '/'+ self.module+'.git')
		output = os.popen('git clone '+ self.url + '/'+ self.module+'.git').read()
		self.logger.log(output)

	def createBranch(self, branch):
		self.git('checkout -b ' + branch)

	def commit(self, message):
		self.git("add .")
		self.git('commit -m  \"' + message + '\"')

	def push(self, branch):
		self.git('push --set-upstream origin ' + branch)

	def createTag(self, version):
		self.git("tag -a " + version + " -m \"release " + version + "\"")

	def pushTag(self):
		self.git('push origin --tags')

	def pullTags(self):
		self.git('fetch --tags')

	def createBranchFromTag(self, tag, branch):
		self.git('checkout tags/'+tag+' -b '+ branch)

	def merge(self, source):
		self.git('merge --strategy-option theirs origin/' + source + ' -m \"merge changes\" ')

	def checkout(self, branch):
		self.git('checkout ' + branch)

	def git(self, command):
		fullCommand = self.client + ' -C ' + self.projectPath + ' ' + command
		self.logger.commandLog(fullCommand)
		if not self.debug:
			output = os.popen(fullCommand).read()
			self.logger.log(output)