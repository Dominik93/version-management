import os
from logger.logger import Logger
from command.command_executor import run
from common.path import *


class Git:

    logger = None

    debug = False
    projectPath = ""
    module = ""
    url = ""
    client = ""

    mergeMessage = 'merge changes'
    mergeCommand = 'merge --strategy-option theirs'

    def __init__(self, config, module, debug=False):
        self.logger = Logger.getInstance()
        self.debug = debug
        self.projectPath = getCurrentDirectory() + '/' + module.split('/')[-1]
        self.module = module
        self.url = config['url']
        self.client = config['client']
        self.mergeCommand = config.get('merge_command', self.mergeCommand)
        self.mergeMessage = config.get('merge_message', self.mergeMessage)
        self.logger.log("Init git with: " + self.projectPath +
         " | " + self.url +
         " | " + self.module + 
         " | client: " + self.client + 
         " | mergeCommand: " + self.mergeCommand + 
         " | mergeMessage: " + self.mergeMessage + 
         " | debug: " + str(self.debug))

    def clone(self):
        self.logger.commandLog('git clone ' + self.url + '/' + self.module+'.git')
        output = os.popen('git clone ' + self.url + '/' + self.module+'.git').read()
        self.logger.log(output)

    def createBranch(self, branch):
        self.git('checkout -b ' + branch)

    def commit(self, message):
        self.git("add .")
        self.git('commit -m  \"' + message + '\"')

    def push(self, branch):
        self.git('push --set-upstream origin ' + branch)

    def createTag(self, version):
        self.git("tag -a " + version + " -m \"release " + version + "\"")

    def pushTag(self):
        self.git('push origin --tags')

    def pullTags(self):
        self.git('fetch --tags')

    def createBranchFromTag(self, tag, branch):
        self.git('checkout tags/'+tag+' -b ' + branch)

    def merge(self, source):
        self.git(self.mergeCommand + ' origin/' + source + ' -m \" ' + self.mergeMessage + ' \" ')

    def checkout(self, branch):
        self.git('checkout ' + branch)

    def git(self, command):
        fullCommand = self.client + ' -C ' + self.projectPath + ' ' + command
        self.logger.commandLog(fullCommand)
        if not self.debug:
            for partOfOutput in run(fullCommand):
                self.logger.log(str(partOfOutput.decode()))
