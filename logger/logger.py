from .file_logger import FileLogger
from .simple_logger import SimpleLogger


class Logger:

    __instance = None

    logger = None

    specialLogDivider = '*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n'

    prettyLogDivider = '-------------------------------------------------------------------------------------\n'

    commandLogDivider = '>>>>>>>>>>        '

    @staticmethod
    def getInstance():
        return Logger.__instance

    @staticmethod
    def initialize(fileLog):
        if Logger.__instance == None:
            Logger(fileLog)
        return Logger.__instance

    def __init__(self, fileLog):
        if Logger.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            if fileLog:
                self.logger = FileLogger(SimpleLogger())
            else:
                self.logger = SimpleLogger()
            Logger.__instance = self

    def log(self, logMessage):
        self.logger.log(logMessage)

    def specialLog(self, logMessage):
        message = self.specialLogDivider + logMessage + '\n' + self.specialLogDivider
        self.logger.log(message)

    def commandLog(self, logMessage):
        self.logger.log(self.commandLogDivider + logMessage + '\n')

    def prettyLog(self, logMessage):
        message = self.prettyLogDivider + logMessage + '\n' + self.prettyLogDivider
        self.logger.log(message)
