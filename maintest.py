from common.Config import Config
from common.Logger import LogManager
from common.File import File
from common.Database import MysqlDB
import logging

if __name__ == '__main__':

    # for interface in interfaces:
    #     if interface.type == 'FILETODB':
    #         db = MysqlDB()
    #         conn = db.pymysql_db()
    #         db.csv_to_db(conn)
    #         connection_info = config.get_db_info()
    #         db.pymysql_db(connection_info)
    #         file.readfile(interface.in)
    #         db.insert(inteface.out)
    #         db.commit()

    #config설정
    config = Config()
    config.readConfig()
    #log설정
    lm = LogManager()
    lm.basicSetting(config)
    lm.logfileSetting(config.get_logpath(), config.get_filesize(), config.get_bucount())
    #파일 변경 및 입출력
    file = File()
    file.readfile(config)
    file.change_file(config)
    file.save_file(config)
    #pymysql DB연동 (csv -> DB, DB->csv)
    mysql = MysqlDB()
    dbc = mysql.dbconnect()
    mysql.db_to_csv(dbc)
    mysql.csv_to_db(dbc)











