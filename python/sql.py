import mysql.connector as sql
con=sql.connect(host='localhost',port=3306,user='root',passwd='root',database='mysql')
cur=con.cursor()
cur.execute("insert into employee values('amit',21,850457654,80000)")
con.commit()
con.close()
print('record inserted')