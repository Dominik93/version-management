import version.version_manager as versionManager
import sys
import os
import configparser
import shutil
import argparse

from init import *
from common.path import getCurrentDirectory
from common.input import Input
from version.version import Version
from logger.logger import Logger
from maven.maven import Maven
from git.git import Git
from git.branch import Branch
from cleaner.cleaner import Cleaner

def releaseModule(customer, module, bumpVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		logger.prettyLog('Release module')
		version = Version(bumpVersion)

		snapshot = 'SNAPSHOT'
		branch = Branch(customer, config['BRANCH'])

		git.clone()
		git.checkout(branch.mainBranch)
		git.merge(branch.developBranch)
		maven.release(customer)
		maven.cleanInstall()
		currentVersion = versionManager.getVersion(module)
		git.commit(currentVersion)
		git.createTag(currentVersion)
		git.checkout(branch.developBranch)
		maven.bumpVersion(prefix = snapshot, version = version)
		currentVersion = versionManager.getVersion(module)
		git.commit('set version to ' + currentVersion)
		git.checkout(branch.mainBranch)
		maven.deploy()

		input.ask("Continue and push changes to branches? Y / N: ")
		git.push(branch.mainBranch)
		git.pushTag()	
		git.checkout(branch.developBranch)
		git.push(branch.developBranch)
	finally:
		cleaner.clean(directory)

	

logger.specialLog('Start release ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)

releaseModule(customer, args.module, args.bump_version)

logger.specialLog('End release ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





