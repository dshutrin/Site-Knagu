import sqlite3 as sql

con = sql.connect('db.sqlite3')
cur = con.cursor()

cur.execute('UPDATE main_sub SET value=0 WHERE id=1')

cur.close()
con.commit()
con.close()