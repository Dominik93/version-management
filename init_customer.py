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

def initCustomer(customer, module):
	directory = getCurrentDirectory() + '/'+ module.split('/')[-1]
	try:
		logger.prettyLog('Init customer')
		branch = Branch(customer)

		git.clone()

		input.ask("Continue and push changes to branches? Y / N: ")
		git.createBranch(branch.develop)
		git.push(branch.develop)
		git.createBranch(branch.master)
		git.push(branch.master)
	finally:
		cleaner.clean(directory)


logger.specialLog('Start init customer ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)
initCustomer(customer, args.module)
logger.specialLog('End init customer ' + args.module + ' ' + str(args.version) + ' ' +  args.bump_version)





