import os
import version_manager as versionManager
from logger import *
from path import *
from version import *
from subprocess import Popen,PIPE,STDOUT,call

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
		self.debug = debug;
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
		version = versionManager.getVersion(self.module)  
		suffixVersion = versionManager.suffix(version) 
		cuttedVersion = versionManager.cutVersion(version)
		versionManager.changeVersion(self.module, version, cuttedVersion)

		self.maven('build-helper:parse-version versions:set ' + self.newVersionBuilder(prefix, Version('incremental')) + ' versions:commit')
				
		version = versionManager.getVersion(self.module)
		versionManager.changeVersion(self.module, version, suffixVersion + '.' + version);
		
	def release(self, prefix):
		self.maven('build-helper:parse-version versions:set ' + self.newVersionBuilder(prefix, Version()) + ' versions:commit')
		
	def releaseSupportVersion(self, prefix):
		version = versionManager.getVersion(self.module)
		suffixVersion = versionManager.suffix(version)
		cuttedVersion = versionManager.cutVersion(version)
		versionManager.changeVersion(self.module, version, cuttedVersion)
		self.maven('build-helper:parse-version versions:set ' + self.newVersionBuilder(prefix, Version()) + ' versions:commit')
		version = versionManager.getVersion(self.module)
		versionManager.changeVersion(self.module, version, suffixVersion + '.' + version);
			
		
	def newVersionBuilder(self, prefix, version):
		if prefix != '':
			prefix = '-' + prefix
			
		versions = [version.majorVersion, version.minorVersion, version.incrementalVersion]
		return '-DnewVersion=' + '.'.join(versions) + '' + prefix

	def maven(self, command):
		fullCommand = self.client +' ' + command +' ' + self.options + ' ' + self.profiles + ' -f ' + self.projectPath
		self.logger.commandLog(fullCommand)
		if not self.debug:
			output = os.popen(fullCommand).read()
			self.logger.log(output)
			if 'BUILD FAILURE' in output:
				raise Exception(fullCommand + ' failed')
		
