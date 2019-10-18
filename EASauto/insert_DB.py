import pymysql
import con_DB
import logging
import datetime

def insert_log_1(num,time=0,result='123123123'):
    con = con_DB.connect_eas_db()
    cur = con.cursor()
    try:
        sql_str = ("INSERT INTO log_1 (num,time,result)"
                   + " VALUES ('%s','%s','%s')" % (num,datetime.datetime.now(),result))
        cur.execute(sql_str)
        con.commit()
    except:
        con.rollback()
        logging.exception('Insert operation error')
        raise
    finally:
        cur.close()
        con.close()

#insert_log_1(1)
#print(datetime.datetime.now())