import version_manager as versionManager
import sys
import os
import configparser
import shutil
import argparse
from git import *
from path import *
from logger import *
from version import *
from branch import *
from maven import *
from input import *
from cleaner import *
from init import *

def createSupportBranch(customer, module, moduleVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		prettyLog('Create support version')
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


specialLog('Start create support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)

args.version = input.askAndAnswer(args.version, 'Set version of module: ');
createSupportBranch(customer, args.module, args.version)

specialLog('End create support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





