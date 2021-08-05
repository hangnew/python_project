import pymysql

def create(datas):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='cnzk0531', db='test')
    cur = con.cursor()
    sql = 'insert into stock(name, now, high, low) values (%s, %s, %s, %s)'
    result = cur.executemany(sql, datas)
    print('처리 결과', result,'개')
    con.commit()
    con.close()

def read():
    con = pymysql.connect(host='localhost', port=3306, user='root', password='cnzk0531', db='test')
    cur = con.cursor()
    sql = 'select * from stock'
    cur.execute(sql)
    rows = cur.fetchall()
    # cur.fetchone()
    # cur.fetchmany(개수)
    return rows
