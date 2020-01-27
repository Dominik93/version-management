import version.version_manager as versionManager
import sys
import os
import configparser
import shutil
import argparse

from init import *
from common.path import getCurrentDirectory
from version.version import Version
from logger.logger import Logger
from maven.maven import Maven
from git.git import Git
from git.branch import Branch
from cleaner.cleaner import Cleaner
from input.input import Input

def releaseSupportBranch(customer, module, moduleVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		logger.prettyLog('Release from support version')
		branch = Branch(customer, moduleVersion)

		git.clone()
		git.checkout(branch.master)
		git.merge(branch.develop)
		maven.releaseSupportVersion(prefix = customer)
		maven.cleanInstall()
		currentVersion = versionManager.getVersion(module)
		git.commit(currentVersion)
		git.createTag(currentVersion)
		git.checkout(branch.develop)
		maven.bumpSupportVersion(prefix ='SNAPSHOT')
		currentVersion = versionManager.getVersion(module)
		git.commit('set version to ' + currentVersion)
		git.checkout(branch.master)
		maven.deploy()

		input.ask("Continue and push changes to branches? Y / N: ")
		git.push(branch.master)
		git.pushTag()
		git.checkout(branch.develop)
		git.push(branch.develop)
	finally:
		cleaner.clean(directory)

logger.specialLog('Start release support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)

args.version = input.askAndAnswer(args.version, 'Set version of module: ');
releaseSupportBranch(customer, args.module, args.version)

logger.specialLog('End release support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





