from common.Config import Config
from common.Logger import LogManager
from common.File import File
from common.Database import MysqlDB
import logging

if __name__ == '__main__':
    try:
        #Config
        config = Config()
        config.readConfig()
        logging.debug('READ CONFIG DONE')
        intf_list = config.get_intf_info()
        logging.debug('GET CONFIG INFO DONE')
        #로그
        logging.debug('LOG SETTING STARTED')
        lm = LogManager()
        lm.basicSetting(config)
        lm.logfileSetting(config.get_logpath(), config.get_filesize(), config.get_bucount())
        logging.debug('LOG SETTING DONE')
        #File
        file = File()
        #DB
        mysql = MysqlDB()
        col_names = config.column_names
        col_renames = config.col_renames
        r_type = config.r_type #required type
        time_condition = config.time_condition
        #파일 입출력
        for intf in intf_list:
            if intf['intf_type'] == 'FILETODB':
                 mysql.dbconnect()
                 logging.debug('FILE TO DB : DB CONNECTED')
                 savepath = intf['savepath']
                 readpath = intf['readpath']
                 mysql.csv_df_db(savepath, readpath, col_names, col_renames)
                 mysql.db_commit()
                 logging.debug('FILE TO DB : DB COMMITTED')
                 mysql.db_close()
                 logging.info("file to db DONE")
            if intf['intf_type'] == 'DBTOFILE':
                savepath = intf['savepath']
                dbc = mysql.dbconnect()
                logging.debug('DB TO FILE : DB CONNECTED')
                r_type = intf['r_type']
                time_condition = intf['time_condition']
                sql_address = intf['sql_address']
                mysql.db_to_csv(savepath, r_type, time_condition, sql_address)
                logging.info("db to file DONE")
            if intf['intf_type'] == 'FILE':
                rpath = intf['readpath']
                spath = intf['savepath']
                file.save_file(spath, rpath)
                logging.info("FILE SAVE DONE")
            elif intf['intf_type'] == 'DBTODB':
                logging.warning("DB TO DB STARTS")
                mysql.dbconnect()
                logging.debug('DB TO DB : DB CONNECTED')
                from_table = config.from_table
                to_table = config.to_table
                mysql.db_to_db(to_table, from_table)
                mysql.db_commit()
                logging.debug('FILE TO DB : DB COMMITTED')
                mysql.db_close()
                logging.info("DB TO DB DONE")
    except Exception as e:
        logging.error(e)