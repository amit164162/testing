import mysql.connector as sql
con=sql.connect(host='localhost',port=3307,user='root',passwd='root',database='')
cur=con.cursor()
cur.execute("insert.into students values(103,'virat',600)")
con.commit()
con.close()
print('record inserted')