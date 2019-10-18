import con_DB
import mysql
import logging

def query_country_name():
    sql_str = ("SELECT * FROM city" )
    logging.info(sql_str)

    con = con_DB.connect_eas_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    #assert len(rows) == 1, 'Fatal error: country_code does not exists!'
    return rows
    #return rows[0][0]

query_country_name()
print(query_country_name())