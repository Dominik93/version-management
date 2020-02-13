from logger.logger import Logger

class VersionBuilder:

	system = ''

	_prefix = None

	_version = None

	def __init__(self, system = 'windows'):
		self.system = system

	def prefix(self, prefix):
		self._prefix = prefix
		return self

	def version(self, version):
		self._version = version	
		return self

	def build(self):
		prefix = ''
		if self._prefix != None:
			if self._prefix != '':
				prefix = '-' + self._prefix

		escape = ''
		if self.system == 'unix':		
			escape = '\\'

		versions = [escape + self._version.majorVersion, escape + self._version.minorVersion, escape + self._version.incrementalVersion]
			
		return '-DnewVersion=' + '.'.join(versions) + '' + prefix
	