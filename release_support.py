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

def releaseSupportBranch(customer, module, moduleVersion):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		prettyLog('Release from support version')
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

specialLog('Start release support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)
args.version = input.askAndAnswer(args.version, 'Set version of module: ');
releaseSupportBranch(customer, args.module, args.version)
specialLog('End release support version ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





