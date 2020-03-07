import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='',
    db='test',
    charset='utf8')

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print("Version is:", data)
