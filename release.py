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

	

logger.specialLog('Start release ' + args.module + ' ' + str(args.version))

releaseModule(args.module, args.version)

logger.specialLog('End release ' + args.module + ' ' + str(args.version))





