import logging
from logging.handlers import RotatingFileHandler

class LogManager():
    def __init__(self):
        self.logger = ""
        self.formatter = ""
        self.stream_handler = ""
        self.level = ""
        self.filehandler = ""
        self.logpath = ""
        self.fsize = 0
        self.bu_count = 0

    def basicSetting(self, config):
        try:
            logging.debug('LOGGER SETTING STARTS')
            self.logger = logging.getLogger()
            self.logger.setLevel(config.get_level())
            self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.stream_handler)
            logging.debug('LOGGER SETTING DONE')
        except Exception as e:
            logging.error(e)

    def logfileSetting(self, logpath, fsize, bu_count):
        try:
            logging.debug('LOGFILE SETTING STARTS')
            if type(fsize) is not int:
                fsize = int(fsize)
            self.filehandler = RotatingFileHandler(logpath, maxBytes=fsize, backupCount=bu_count)
            self.filehandler.setFormatter(self.formatter)
            self.logger.addHandler(self.filehandler)
            logging.debug('LOGFILE SETTING STARTS')
        except Exception as e:
            logging.error(e)


