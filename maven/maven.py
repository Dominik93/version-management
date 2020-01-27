import os
import common.path
from logger.logger import Logger
from version.version import Version
from common.path import getCurrentDirectory
from subprocess import Popen,PIPE,STDOUT,call
from command.command_executor import run
from version.version_manager import (changeVersion,incrementVersion, getVersion, suffix, cutVersion)

class Maven:

	logger = None

	debug = False
	projectPath = ""
	module = ""
	client = ""
	options = ""
	profiles = ""

	def __init__(self, config, module, options, profiles, debug = False):
		self.logger = Logger.getInstance()
		self.debug = debug
		self.projectPath = getCurrentDirectory() + '/'+ module.split('/')[-1]
		self.client = config['MAVEN']['client']
		self.module = module
		self.options = options.replace('\'','')
		self.profiles = profiles.replace('\'','')
		self.logger.log("Init maven with: " + self.projectPath + " | " + self.module + " | options: " + self.options + " | profiles: " + self.profiles + " | client: " + self.client + " | debug: " +str(self.debug))

	def cleanInstall(self):
		self.maven('clean install')

	def deploy(self):
		if not self.debug:
			self.maven('install')

	def bumpVersion(self, prefix, version):
		self.maven('build-helper:parse-version versions:set ' + self.newVersionBuilder(prefix, version) + ' versions:commit')
		
	def bumpSupportVersion(self, prefix):
		version = getVersion(self.module)  
		suffixVersion = suffix(version) 
		cuttedVersion = cutVersion(version)
		changeVersion(self.module, version, cuttedVersion)

		self.maven('build-helper:parse-version versions:set ' + self.newVersionBuilder(prefix, Version('incremental')) + ' versions:commit')
				
		version = getVersion(self.module)
		changeVersion(self.module, version, suffixVersion + '.' + version);
		
	def release(self, prefix):
		self.maven('build-helper:parse-version versions:set ' + self.newVersionBuilder(prefix, Version()) + ' versions:commit')
		
	def releaseSupportVersion(self, prefix):
		version = getVersion(self.module)
		suffixVersion = suffix(version)
		cuttedVersion = cutVersion(version)
		changeVersion(self.module, version, cuttedVersion)
		self.maven('build-helper:parse-version versions:set ' + self.newVersionBuilder(prefix, Version()) + ' versions:commit')
		version = getVersion(self.module)
		changeVersion(self.module, version, suffixVersion + '.' + version);
			
		
	def newVersionBuilder(self, prefix, version):
		if prefix != '':
			prefix = '-' + prefix
			
		versions = [version.majorVersion, version.minorVersion, version.incrementalVersion]
		return '-DnewVersion=' + '.'.join(versions) + '' + prefix

	def maven(self, command):
		fullCommand = self.client +' ' + command +' ' + self.options + ' ' + self.profiles + ' -f ' + self.projectPath
		self.logger.commandLog(fullCommand)
		if not self.debug:
			for partOfOutput in run(fullCommand):
				self.logger.log(str(partOfOutput.decode()))
				if 'BUILD FAILURE' in str(partOfOutput.decode()):
					raise Exception(fullCommand + ' failed')
		