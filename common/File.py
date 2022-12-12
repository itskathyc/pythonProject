import logging
import csv

class File():
    def __init__(self):
        pass

    def change_file(self, readpath):
        logging.info('changefile started')
        try:
            openfile = open(readpath, 'r')
            cfile = openfile.read().replace(',', '|')
            return cfile
            logging.info('changefile ended')
        except Exception as e:
            raise

    def save_file(self, spath, readpath):
        logging.info('savefile started')
        try :
            cfile = self.change_file(readpath)
            spath = spath
            f = open(spath, 'w')
            f.write(cfile)
            f.close()
            logging.info('savefile ended')
        except Exception:
            raise
