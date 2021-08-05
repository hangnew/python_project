import pymysql

con = pymysql.connect(host='localhost', user='root', password='cnzk0531', db='test', charset='utf8')
cur = con.cursor()

sql = "insert into member values('melon');"
result = cur.execute(sql)
con.commit()
con.close()
