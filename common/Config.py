import logging
import xml.etree.ElementTree as ET

class Config:
    path = ET.parse('C:/Users/cdy16/PycharmProjects/pythonProject/config/config.xml')
    root = path.getroot()

    def __init__(self):
        self.filesize = 0
        self.bucount = 0
        self.level = ""
        self.intf_list = []
        self.logpath = ""
        self.readpath = ""
        self.savepath = ""
        self.db_connection_info = {}
        self.column_names = []
        self.col_renames = []
        self.rename = ""
        self.name = ""
        self.sql = ""
        self.from_table = ""
        self.to_table = ""

    def readConfig(self):
        try :
            root = self.path.getroot()
            for common in root.findall("common"):
                logger = common.find("logger")
                self.logpath = logger.attrib.get("path")
                self.filesize = logger.attrib.get("file_size")
                self.bucount = logger.attrib.get("count")
                self.level = logger.attrib.get("level")
            for conn in root.findall("connection"):
                db = conn.find("db")
                self.db_connection_info['host'] = db.attrib.get("host")
                self.db_connection_info['port'] = db.attrib.get("port")
                self.db_connection_info['user'] = db.attrib.get("user")
                self.db_connection_info['password'] = db.attrib.get("password")
                self.db_connection_info['db'] = db.attrib.get("db")
                self.db_connection_info['charset'] = db.attrib.get("charset")
            for intfs in root.findall("interfaces/interface"):
                intf_dict = {}
                intf_dict['intf_type'] = intfs.attrib.get("type")
                intf_dict['readpath'] = intfs.attrib.get("in")
                intf_dict['savepath'] = intfs.attrib.get("out")
                intf_dict['required_date'] = intfs.attrib.get("required_date")
                intf_dict['required_time'] = intfs.attrib.get("required_time")
                self.intf_list.append(intf_dict)
            #
            for col in root.findall("interfaces/interface/columns/column"):
                self.name = col.attrib.get("name")
                self.column_names.append(self.name)
                self.rename = col.attrib.get("rename")
                self.col_renames.append(self.rename)
            #db to db
            for sql in root.findall("interfaces/interface/sql"):
                #fromtable_info, totable_info를 리스트로 받으면?
                self.from_table = sql.attrib.get("from_table")
                self.to_table = sql.attrib.get("to_table")
        except Exception as e:
            logging.error('READ CONFIG : ', e)
            raise

    def get_db_info(self):
        try:
            return self.connection_info
        except Exception as e:
           logging.error('CONFIG - GET DB INFO : ', e)
           raise

    def get_logpath(self):
        try:
            return self.logpath
        except Exception as e:
           logging.error('CONFIG - GET LOGPATH : ', e)
           raise

    def get_intf_info(self):
        try:
            return self.intf_list
        except Exception as e:
            logging.error('CONFIG - GET_CONFIGXML_INTF_INFO : ', e)
            raise

    def get_intftype(self):
        try:
            return self.intf_type
        except Exception as e:
            logging.error('CONFIG - GET_INTFTYPE : ', e)
            raise

    def get_filesize(self):
        try:
            return self.filesize
        except Exception as e:
            logging.error('CONFIG - READ CONFIG', e)
            raise

    def get_bucount(self):
        try:
            return self.bucount
        except Exception as e:
            logging.error('CONFIG - GET_BACKUP_COUNT : ', e)
            raise

    def get_readpath(self):
        try:
            return self.readpath
        except Exception as e:
            logging.error('CONFIG - GET_READPATH : ', e)
            raise

    def get_savepath(self):
        try:
            return self.savepath
        except Exception as e:
            logging.error('CONFIG - GET_SAVEPATH : ', e)
            raise

    def get_level(self):
        try:
            return self.level
        except Exception as e:
            logging.error('CONFIG - GET_LOGLEVEL : ', e)
            raise

    def get_db_conn_info(self):
        try:
            return self.db_connection_info
        except Exception as e:
            logging.error('CONFIG - GET_DB_CONN_INFO : ', e)
            raise

    def get_column_name(self):
        try:
            return self.column_nms
        except Exception as e:
            logging.error('CONFIG - GET_COLUMN_NAME: ', e)
            raise

    def get_table_info(self):
        try:
            return self.table_info
        except Exception as e:
            logging.error('CONFIG - GET_TABLE_INFO : ', e)
            raise

    def get_sql(self):
        try:
            return self.sql
        except Exception as e:
            logging.error('CONFIG - GET_SQL : ', e)
            raise

    def get_currentdates(self):
        try :
            return self.current_dates
        except Exception as e:
            logging.error('CONFIG - GET_CURRENTDATES : ', e)
            raise