CAMPAIGNS = {
    "balance transfer ? nca campaign": 442
}
import pymysql
import re
DB_HOST = 'localhost'
DB_NAME = 'test'
DB_PASSWORD = 'pass'
DB_PORT = 3306
DB_USER = 'tuser'

if __name__ == "__main__":
    query = "insert into ICICI_campaigns(name, account) Values"
    for i in CAMPAIGNS.keys():
        val = re.sub('[^0-9a-z ]+', '', i)
        query += "('" + val + "'," + str(CAMPAIGNS[i]) + "),"
    query = query[:-1] + ";"
    sql_conn = pymysql.connect(
                        host=DB_HOST,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        db=DB_NAME,
                        port=DB_PORT
                    )
    sql_cur = sql_conn.cursor()
    sql_cur.execute(query)
    agent = sql_conn.commit()
