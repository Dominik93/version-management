
class FileLogger:

    logger = None

    file = None

    def __init__(self, logger):
        self.logger = logger
        self.file = open("log.txt", "w+")

    def __del__(self):
        self.file.close()

    def log(self, logMessage):
        self.logger.log(logMessage)
        self.file.write(logMessage+'\n')
