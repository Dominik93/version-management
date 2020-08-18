import sys
import os
import configparser
import shutil
import argparse
import platform
from logger.logger import Logger
from maven.maven import Maven
from git.git import Git
from cleaner.cleaner import Cleaner
from common.input import Input

parser = argparse.ArgumentParser(description='Tool for version management')
parser.add_argument("module", help = 'Module to release')
parser.add_argument("--config-file", help = 'Configuration file, default config.ini', default = 'config.ini')
parser.add_argument("--version", help = 'New version of module')
parser.add_argument("--debug-mode", help = 'Debug mode, don`t execute command like git push, mvn clean install', action='store_true')
parser.add_argument("--log-output", help = 'Log all executed command and messages into file log.txt', action='store_true')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config_file)

system = platform.system().lower()
logger = Logger.initialize(args.log_output)

logger.prettyLog('Init variables')
git = Git(config['GIT'], args.module, args.debug_mode)
maven = Maven(config['MAVEN'], args.module, args.debug_mode)
input = Input(False)
cleaner = Cleaner(system)
logger.prettyLog('Init variables end')
