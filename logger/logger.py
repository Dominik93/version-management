from .file_logger import FileLogger
from .simple_logger import SimpleLogger


class Logger:

    __instance = None

    fileLogger = None
    simpleLogger = None

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
            self.fileLogger = FileLogger(fileLog)
            self.simpleLogger = SimpleLogger()
            Logger.__instance = self

    def log(self, logMessage):
        self.simpleLogger.log(logMessage)
        self.fileLogger.log(logMessage+'\n')

    def specialLog(self, logMessage):
        message = '*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n' + \
            logMessage+'\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n'
        self.simpleLogger.log(message)
        self.fileLogger.log(message)

    def commandLog(self, logMessage):
        self.simpleLogger.log('>>>>>>>>>>     ' + logMessage + '\n')
        self.fileLogger.log('>>>>>>>>>>     ' + logMessage + '\n')

    def prettyLog(self, logMessage):
        message = '-------------------------------------------------------------------------------------\n' + \
            logMessage+'\n-------------------------------------------------------------------------------------\n'
        self.simpleLogger.log(message)
        self.fileLogger.log(message)
