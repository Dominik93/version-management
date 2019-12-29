from logger import *

versions = ['major', 'minor', 'incremental']
defaultVersion = 'incremental'

class Version:
	incrementMajorVersion = False
	incrementMinorVersion = False
	incrementIncrementalVersion = False

	majorVersion = '${parsedVersion.majorVersion}'
	minorVersion = '${parsedVersion.minorVersion}'
	incrementalVersion = '${parsedVersion.incrementalVersion}'

	def __init__(self, bumpedVersion = 'none'):
		if bumpedVersion == "major":
			self.incrementMajorVersion = True
			self.majorVersion = '${parsedVersion.nextMajorVersion}'
		elif bumpedVersion == "minor":
			self.incrementMinorVersion = True
			self.minorVersion = '${parsedVersion.nextMinorVersion}'
		elif bumpedVersion == "incremental":
			self.incrementIncrementalVersion = True
			self.incrementalVersion = '${parsedVersion.nextIncrementalVersion}'
		log('Init version with: ' + str(self.incrementMajorVersion) +" | " + str(self.incrementMinorVersion) +" | "+ str(self.incrementIncrementalVersion) + ' | ' + self.majorVersion+ '.' + self.minorVersion+ '.' + self.incrementalVersion)