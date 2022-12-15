import logging

import pymysql
import csv
import pandas as pd
from sqlalchemy import create_engine
import datetime

class MysqlDB():
    def __init__(self):
        self.conn = 0
        self.cursor = 0

    def dbconnect(self):
        try:
            self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='emp', charset='utf8')
            db_connection_str = "mysql+pymysql://root:password@localhost/emp"
            db_connection = create_engine(db_connection_str)
            logging.debug('DB CONNECTED')
            return db_connection
        except Exception as err:
            logging.error('MysqlDB - DBCONNECT : ', err)
            raise

    def csv_df_db(self, savepath, readpath, o_names, n_names):
        try :
            logging.debug('CSV_TO_DB STARTED')
            cursor = self.conn.cursor()
            db_connection = self.dbconnect()
            # schema_name = "emp" >> 위에 dbconnect 에서 db를 지정했기 때문에 여기서 재정의 불필요
            table_name = savepath
            #db컬럼명만 추출하는 쿼리
            sql = f"""select column_name from information_schema.columns where table_name = '{table_name}'"""
            cursor.execute(sql.format(table_name))
            logging.debug('SQL EXECUTED : DB컬럼명 추출')
            colname_df = pd.read_sql_query(sql, self.conn)
            cname = colname_df.values.tolist() #db에 저장된 컬럼명이 2중리스트로 담긴다 : [['Department'], ['Email'], ['Name'], ['Salary']]
            cnames=[j for i in cname for j in i]
            file = open(readpath, 'r')
            csvfile = pd.read_csv(file)
            # rename 값이 있을 시 변경
            for alias in n_names:
                if alias:
                    csvfile.rename(columns={o_names[n_names.index(alias)] : alias}, inplace=True)
            logging.debug('COLUMN NAME CHANGED TO ALIAS')
            #csv헤더 중 db컬럼명에 해당하는 것만 추출 & DB insert - 이 때 csv헤더와 db컬럼명의 대소문자도 구분되니 주의
            input = csvfile[cnames]
            input.to_sql(name=savepath, con=db_connection, if_exists='append', index=False)
            logging.debug('CSV_TO_DB DONE')
        except Exception as e:
            logging.error('MysqlDB - CSV_DF_DB : ', e)
            raise

    def db_to_csv(self, savepath, r_type, time_condition, sql_address):
        try:
            cursor = self.conn.cursor()
            currdate = datetime.datetime.now().strftime('%Y-%m-%d')
            currdate_hour = datetime.datetime.now().strftime('%Y-%m-%d %H')
            sql = ""
            if sql_address:
                openquery = open(sql_address, 'r')
                query = openquery.readline()
                if ':CURRENTDATETIME' in query:
                    logging.debug('READ SQL FROM FILE - DATETIME')
                    sql = query.replace(':CURRENTDATETIME', "'" + currdate_hour + "'")
                elif ':CURRENTDATE' in query:
                    logging.debug('READ SQL FROM FILE - DATE')
                    sql = query.replace(':CURRENTDATE', "'" + currdate + "'")
            elif r_type:
                if time_condition == 'CURRENTDATE':
                    logging.debug('READ SQL FROM CONFIG - DATE')
                    sql = f"select * from employee where DATE_FORMAT(JoinDatetime, '%Y-%m-%d') = '{currdate}';"
                    cursor.execute(sql.format(currdate))
                elif time_condition == 'CURRENTTIME':
                    logging.debug('READ SQL FROM CONFIG - DATETIME')
                    sql = f"select * from employee where JoinDatetime = '{currdate_hour}'"
                    cursor.execute(sql.format(currdate_hour))
            else:
                sql = """SELECT * from employee"""
            df = pd.read_sql_query(sql, self.conn)
            df.to_csv(savepath, index=False)
        except Exception as e:
            logging.error('MysqlDB - DB TO CSVFILE : ', e)
            raise

    def db_to_db(self, to_table, from_table):
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO {0} SELECT * FROM {1}"
            cursor.execute(sql.format(to_table, from_table))
        except Exception as e:
            logging.error('MysqlDB - DB TO DB : ', e)
            raise

    def db_commit(self):
        try :
            self.conn.commit()
        except Exception as e:
            logging.error('MysqlDB - DB COMMIT : ', e)
            raise

    def db_close(self):
        try :
            self.conn.close()
        except Exception as e:
            logging.error('MysqlDB - DB CLOSE : ', e)
            raise
