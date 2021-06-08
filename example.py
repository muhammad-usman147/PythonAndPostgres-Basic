import psycopg2 as py

con = py.connect(
    host = 'localhost',
    database = 'firstdatabase',
    user = 'postgres',
    password = 'usman1234'
)

cur = con.cursor()

cur.execute('Select * from karachi')
rows = cur.fetchall()
for r in rows:
    print(r)

cur.close()
con.close()

