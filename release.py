import sys
import os
import configparser
import shutil
import argparse

from init import *
from common.path import getCurrentDirectory
from common.input import Input
from logger.logger import Logger
from maven.maven import Maven
from git.git import Git
from git.branch import Branch
from cleaner.cleaner import Cleaner

def releaseModule(module, bumpVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		logger.prettyLog('Release module')

		branch = Branch(config['BRANCH'])

		git.clone()
		git.checkout(branch.mainBranch)
		maven.bumpVersion(bumpVersion)
		git.commit('v ' + bumpVersion)
		git.createTag(bumpVersion)
		input.ask("Continue and push changes to branches? Y / N: ")
		git.push(branch.mainBranch)
		git.pushTag()
	finally:
		cleaner.clean(directory)

	
def printModules(projects):
	i = 1
	print('0-None')
	for key in projects.keys():
		print(str(i) +'-' + key)
		i += 1

def getPoject(projects, index):
	i = 1
	for key in projects.keys():
		if str(i) == index:
			return projects[key]
	return 'None'		
			

while True:
	printModules(config['PROJECT'])
	module = getPoject(config['PROJECT'], input.askAndAnswer(None, "Choose module: "))
	print(module)
	if module == 'None':
		break
	version = input.askAndAnswer(None, "Choose version: ")
	git = Git(config['GIT'], module, args.debug_mode)
	maven = Maven(config['MAVEN'], module, args.debug_mode)
	logger.specialLog('Start release ' + module + ' ' + str(version))
	releaseModule(module, version)
	logger.specialLog('End release ' + module + ' ' + str(version))





