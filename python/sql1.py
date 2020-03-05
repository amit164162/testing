import mysql as sql
con=con.cursor()
cur.execute("select * from students where marks>=700 ")
print