import sys
import os
import configparser
import shutil
import argparse
from logger.logger import Logger
from maven.maven import Maven
from git.git import Git
from cleaner.cleaner import Cleaner
from input.input import Input
from version.version import (defaultVersion, versions)

parser = argparse.ArgumentParser(description='Tool for version management')
parser.add_argument("module", help = 'Module to release')
parser.add_argument("--config-file", help = 'Configuration file, default config.ini', default = 'config.ini')
parser.add_argument("--version", help = 'Support version of module, needed only from support versions')
parser.add_argument("--maven-options", help = 'Options pass to maven, eg. "-DskipTests"', default='')
parser.add_argument("--maven-profiles", help = 'Profiles pass to maven, eg. "-PWAS"', default='')
parser.add_argument("--bump-version", help = 'What version number will be bump, only for release' , choices = versions, default = defaultVersion)
parser.add_argument("--silent", help = 'Silent mode. Never ask user for input', action='store_true')
parser.add_argument("--debug-mode", help = 'Debug mode, don`t execute command like git clone, mvn clean install', action='store_true')
parser.add_argument("--log-output", help = 'Log all executed command and messages into file', action='store_true')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config_file)
logger = Logger.initialize(args.log_output)
logger.prettyLog('Init variables')
customer = config['PROJECT']['customer']
logger.log('Customer ' + customer)
git = Git(config, args.module, args.debug_mode)
maven = Maven(config, args.module, args.maven_options, args.maven_profiles, args.debug_mode)
input = Input(args.silent)
cleaner = Cleaner(config['ENV']['system'])
logger.prettyLog('Init variables end')
