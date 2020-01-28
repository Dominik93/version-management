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

def releaseSupportBranch(customer, module, moduleVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		logger.prettyLog('Release from support version')
		branch = Branch(customer, config['BRANCH'], moduleVersion)

		git.clone()
		git.checkout(branch.mainBranch)
		git.merge(branch.developBranch)
		maven.releaseSupportVersion(prefix = customer)
		maven.cleanInstall()
		currentVersion = versionManager.getVersion(module)
		git.commit(currentVersion)
		git.createTag(currentVersion)
		git.checkout(branch.developBranch)
		maven.bumpSupportVersion(prefix ='SNAPSHOT')
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

logger.specialLog('Start release support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)

args.version = input.askAndAnswer(args.version, 'Set version of module: ')
releaseSupportBranch(customer, args.module, args.version)

logger.specialLog('End release support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





