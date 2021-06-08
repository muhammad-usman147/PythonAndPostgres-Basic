import psycopg2 as pgpy

con = pgpy.connect(
    host = 'localhost',
    database = 'firstdatabase',
    user = 'postgres',
    password = 'usman1234'
)
#creating cursor
cur = con.cursor()


#cur.execute("Insert into karachi(id,person, city) values( %s, %s, %s)", (2, 'Saad Alam', 'Ghotki'))
#con.commit()

#select query

cur.execute("Select * from karachi") #karachi is the table name
rows = cur.fetchall()

for i in rows:
    print(i)


cur.close()

con.close()