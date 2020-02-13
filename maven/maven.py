import os
import common.path
from logger.logger import Logger
from version.version import Version
from version.version_builder import VersionBuilder
from common.path import getCurrentDirectory
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

	versionBuilder: VersionBuilder = None

	deployCommand = 'deploy'
	installCommand = 'clean install'

	def __init__(self, config, module, options, profiles, system, debug = False):
		self.logger = Logger.getInstance()
		self.versionBuilder = VersionBuilder(system)
		self.debug = debug
		self.projectPath = getCurrentDirectory() + '/'+ module.split('/')[-1]
		self.client = config['client']
		self.deployCommand = config.get('deploy_command', self.deployCommand)
		self.installCommand = config.get('install_command', self.installCommand)
		self.module = module
		self.options = options.replace('\'','')
		self.profiles = profiles.replace('\'','')
		self.logger.log("Init maven with: " + self.projectPath + " | " + self.module + 
		" | options: " + self.options + 
		" | profiles: " + self.profiles + 
		" | client: " + self.client + 
		" | deployCommand: " + self.deployCommand + 
		" | installCommand: " + self.installCommand + 
		" | debug: " +str(self.debug))

	def cleanInstall(self):
		self.maven(self.installCommand)

	def deploy(self):
		self.maven(self.deployCommand)

	def bumpVersion(self, prefix, version):
		self.maven('build-helper:parse-version versions:set ' + self.versionBuilder.prefix(prefix).version(version).build() + ' versions:commit')
		
	def bumpSupportVersion(self, prefix):
		version = getVersion(self.module)  
		suffixVersion = suffix(version) 
		cuttedVersion = cutVersion(version)
		changeVersion(self.module, version, cuttedVersion)

		self.maven('build-helper:parse-version versions:set ' + self.versionBuilder.prefix(prefix).version(Version('incremental')).build() + ' versions:commit')
				
		version = getVersion(self.module)
		changeVersion(self.module, version, suffixVersion + '.' + version)
		
	def release(self, prefix):
		self.maven('build-helper:parse-version versions:set ' + self.versionBuilder.prefix(prefix).version(Version()).build()  + ' versions:commit')
		
	def releaseSupportVersion(self, prefix):
		version = getVersion(self.module)
		suffixVersion = suffix(version)
		cuttedVersion = cutVersion(version)
		changeVersion(self.module, version, cuttedVersion)
		self.maven('build-helper:parse-version versions:set ' + self.versionBuilder.prefix(prefix).version(Version()).build()  + ' versions:commit')
		version = getVersion(self.module)
		changeVersion(self.module, version, suffixVersion + '.' + version)
			
	def maven(self, command):
		fullCommand = self.client +' ' + command +' ' + self.options + ' ' + self.profiles + ' -f ' + self.projectPath
		self.logger.commandLog(fullCommand)
		if not self.debug:
			for partOfOutput in run(fullCommand):
				self.logger.log(str(partOfOutput.decode()))
				if 'BUILD FAILURE' in str(partOfOutput.decode()):
					raise Exception(fullCommand + ' failed')
		
