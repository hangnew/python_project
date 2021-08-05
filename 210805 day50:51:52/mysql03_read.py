import mysql02_db as db

rows = db.read()
print(rows)
print(type(rows))

for row in rows:
    print(row[0], str(row[1]) + '원', row[2], row[3])
