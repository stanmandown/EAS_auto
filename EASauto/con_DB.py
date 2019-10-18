import pymysql
import logging

def connect_eas_db():
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='p@ssw0rd',
                           database='eas_auto')


#db=pymysql.connect("localhost","root","p@ssw0rd","world")

# 使用 cursor() 方法创建一个游标对象 cursor
#cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
#cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()

#print("Database version : %s " % data)

# 关闭数据库连接
#db.close()

"""def query_country_name(cc2):
    sql_str = ("SELECT Fcountry_name_zh"
                + " FROM t_country_code"
                + " WHERE Fcountry_2code='%s'" % (cc2))
    logging.info(sql_str)

    con = con_DB.connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    assert len(rows) == 1, 'Fatal error: country_code does not exists!'
    return rows[0][0]"""