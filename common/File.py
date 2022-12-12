import logging
import csv

class File():
    def __init__(self):
        pass

    # def readfile(self, config):
    #     logging.info('readfile started')
    #     try:
    #         readpath = config.readpath #None으로 넘어옴 : for문으로 돌렸기 때문. dictionary에 담아서 정확한 key-value를 찾아주니 해결
    #         rfile = open(readpath, 'r')
    #         return rfile
    #     except Exception as e:
    #         logging.warning(e)
    #     logging.info('readfile ended')

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
