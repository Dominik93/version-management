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


def createSupportBranch(customer, module, moduleVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		logger.prettyLog('Create support version')
		branch = Branch(customer, moduleVersion)

		git.clone()
		git.pullTags()
		git.createBranchFromTag(moduleVersion + "-" + customer.upper(), branch.master)
		versionManager.incrementVersion(module)
		maven.cleanInstall()
		currentVersion = versionManager.getVersion(module)
		git.commit('release version ' + currentVersion)
		git.createTag(currentVersion)
		maven.deploy()

		input.ask("Continue and push changes to branches? Y / N: ")
		git.push(branch.master)
		git.pushTag()
		git.createBranch(branch.develop)
		maven.bumpSupportVersion(prefix = 'SNAPSHOT')
		currentVersion = versionManager.getVersion(module)
		git.commit('set version to ' + currentVersion)
		git.push(branch.develop)
	finally:
		cleaner.clean(directory)


logger.specialLog('Start create support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)

args.version = input.askAndAnswer(args.version, 'Set version of module: ')
createSupportBranch(customer, args.module, args.version)

logger.specialLog('End create support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





