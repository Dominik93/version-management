from os import walk
from logger import *
from path import *
import os
import shutil

skippedPomFragments = ['<parent>', '<dependency>']
endSkippedPomFragments = ['</parent>', '</dependency>']


def incrementVersion(module):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	currentVersion = getVersion(module);
	incrementedVersion = insertZero(currentVersion)
	logger.log('Increment version of '+ module + ' from ' + currentVersion + ' to ' + incrementedVersion)
	changeVersion(module, currentVersion, incrementedVersion)


def changeVersion(module, oldVersion, newVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	changeMainVersion(directory + '/pom.xml', oldVersion, newVersion)
	for (dirpath, dirnames, filenames) in walk(directory):
		if 'pom.xml' in filenames and directory != dirpath:
			changeParentVersion(dirpath + '/pom.xml', oldVersion, newVersion)
	
	
def changeParentVersion(file, currentVersion, incrementedVersion):
	f = open(file, "r") 
	ignore = False
	lines = f.readlines()
	f.close()
	
	f = open(file,'w')
	for line in lines:
		if isInArray(["<dependency>", "</parent>"], line):
			ignore = True
		if isInArray(["<parent>", "</dependency>"], line):
			ignore = False
		if not ignore and "<version>" in line:
			f.write(line.replace(currentVersion, incrementedVersion))
		else:
			f.write(line)
	f.close()
	logger.log('Changed parent in file '+ file + ' from ' + currentVersion + ' to ' + incrementedVersion)
	
def changeMainVersion(file, currentVersion, incrementedVersion):
	f = open(file, "r") 
	ignore = False
	lines = f.readlines()
	f.close()
	
	f = open(file,'w')
	for line in lines: 
		if isInArray(skippedPomFragments, line):
			ignore = True
		if isInArray(endSkippedPomFragments, line):
			ignore = False
		if not ignore and "<version>" in line:
			f.write(line.replace(currentVersion, incrementedVersion))
		else:
			f.write(line)
	f.close()
	logger.log('Changed main pom '+ file + ' from ' + currentVersion + ' to ' + incrementedVersion)
		
def getVersion(module):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	file = open(directory+ "/pom.xml", "r") 
	version = ""
	ignore = False
	for line in file: 
		if isInArray(skippedPomFragments, line):
			ignore = True
		if isInArray(endSkippedPomFragments, line):
			ignore = False
		if not ignore and "<version>" in line:
			version = line.strip().strip("<version>").strip("</version>")
			break

	file.close()
	logger.log('Get version ' + version)
	return version;

def cutVersion(version):
	prefix = version.split('-')[1]
	ver = version.split('-')[0]
	if len(ver.split('.')) > 3: # 1.2.5.4.5.8
		index = ver.rfind('.', 0, ver.rfind('.', 0, ver.rfind('.') -1) -1)
		cut = '-'.join([ver[index+1:], prefix])
		logger.log('Cut: ' + cut)
		return cut
	cut = '-'.join([ver, prefix])
	logger.log('Cut: ' + cut)
	return cut
	
def suffix(version):
	prefix = version.split('-')[1]
	ver = version.split('-')[0]
	if len(ver.split('.')) > 3: # 1.2.5.4.5.8
		index = ver.rfind('.', 0, ver.rfind('.', 0, ver.rfind('.') -1) -1)
		suffix = ver[:index]
		logger.log('Suffix: ' + suffix)
		return suffix
	suffix = ver
	logger.log('Suffix: ' + suffix)
	return suffix

	
def insertZero(version):
	prefix = version.split('-')[1]
	ver = version.split('-')[0]
	ver = ver + '.0'
	return '-'.join([ver, prefix])

def isInArray(items, array):
	for item in items:
		if item in array:
			return True
	return False