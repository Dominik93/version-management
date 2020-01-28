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

def initCustomer(customer, module):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		logger.prettyLog('Init customer')
		branch = Branch(customer, config['BRANCH'])

		git.clone()

		input.ask("Continue and push changes to branches? Y / N: ")
		git.createBranch(branch.developBranch)
		git.push(branch.developBranch)
		git.createBranch(branch.mainBranch)
		git.push(branch.mainBranch)
	finally:
		cleaner.clean(directory)


logger.specialLog('Start init customer ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)
initCustomer(customer, args.module)
logger.specialLog('End init customer ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





