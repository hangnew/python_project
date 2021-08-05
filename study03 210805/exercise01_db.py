import pymysql

def create(datas):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='cnzk0531', db='test')
    cur = con.cursor()
    sql = 'insert into book(title, price) values (%s, %s)'
    result = cur.executemany(sql, datas)
    print('처리 결과:', result)
    con.commit()
    con.close()
